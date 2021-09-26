from typing import TYPE_CHECKING, Optional, Type, List, Set
from copy import copy
import logging
import os

from lona.static_files import StyleSheet, StaticFile, Script
from lona.imports import get_all_subclasses, get_file
from lona.html.abstract_node import AbstractNode

# avoid import cycles
if TYPE_CHECKING:
    from lona.server import LonaServer


logger = logging.getLogger('lona.static_file_loader')


class StaticFileLoader:
    def __init__(self, server: 'LonaServer') -> None:
        self.server: 'LonaServer' = server

        self.static_dirs: List[str] = [
            *self.server.settings.STATIC_DIRS,
            *self.server.settings.CORE_STATIC_DIRS,
        ]

        # resolving potential relative paths
        for index, static_dir in enumerate(self.static_dirs):
            self.static_dirs[index] = self.server.resolve_path(static_dir)

        logger.debug('static dirs %s loaded', repr(self.static_dirs)[1:-1])

        self.discover()

    def discover_node_static_files(self) -> None:
        self.node_stylesheets: List[StyleSheet] = []
        self.node_scripts: List[Script] = []
        self.node_static_files: List[StaticFile] = []
        self.static_files: List[StaticFile] = []

        # discover
        discovered_names: Set[str] = set()
        # can't use set because StaticFileDecl is unhashable
        visited_declarations: List[StaticFile] = []

        for node_class in self.node_classes:
            for file_declaration in node_class.STATIC_FILES:
                node_class_path = get_file(node_class)
                node_class_dirname = os.path.dirname(node_class_path)

                # check static file
                if not isinstance(file_declaration, StaticFile):
                    logger.error(
                        '%s::%s: unknown type found: %r',
                        node_class_path,
                        node_class.__name__,
                        file_declaration,
                    )

                    continue

                if file_declaration in visited_declarations:
                    continue

                visited_declarations.append(file_declaration)

                if file_declaration.name in discovered_names:
                    logger.error(
                        "%s::%s: static file with name '%s' already used",
                        node_class_path,
                        node_class.__name__,
                        file_declaration.name,
                    )

                    continue

                # create a local copy
                static_file = copy(file_declaration)

                static_file.static_url_prefix = \
                    self.server.settings.STATIC_URL_PREFIX

                # patch path
                static_file_rel_path = static_file.path

                static_file_abs_path = os.path.join(
                    node_class_dirname, static_file_rel_path)

                if not os.path.exists(static_file_abs_path):
                    logger.error(
                        "%s::%s: path '%s' does not exist",
                        node_class_path,
                        node_class.__name__,
                        static_file_abs_path,
                    )

                    continue

                static_file.path = static_file_abs_path

                # patch url
                if not static_file.url:
                    url = static_file_rel_path

                else:
                    url = static_file.url

                if url.startswith('/'):
                    url = url[1:]

                static_file.url = url

                # disable static files that are not enabled by default and
                # are not configured to be enabled
                if(not static_file.enabled_by_default and
                   static_file.name not in
                   self.server.settings.STATIC_FILES_ENABLED):

                    static_file.enabled = False

                # disable static files that are disabled explicitly
                if static_file.name in self.server.settings.STATIC_FILES_DISABLED:  # NOQA: LN001
                    static_file.enabled = False

                # sort static file into the right cache
                if isinstance(static_file, StyleSheet):
                    self.node_stylesheets.append(static_file)

                elif isinstance(static_file, Script):
                    self.node_scripts.append(static_file)

                else:
                    self.node_static_files.append(static_file)

                discovered_names.add(static_file.name)

        # sort
        self.node_stylesheets.sort(key=lambda x: x.sort_order.value)
        self.node_scripts.sort(key=lambda x: x.sort_order.value)
        self.node_static_files.sort(key=lambda x: x.sort_order.value)

        self.static_files = [
            *self.node_stylesheets,
            *self.node_scripts,
            *self.node_static_files,
        ]

    def discover(self) -> None:
        logger.debug('discover node classes')

        self.node_classes: List[Type[AbstractNode]] = [AbstractNode] + list(get_all_subclasses(AbstractNode))  # NOQA: LN001
        self.discover_node_static_files()

        logger.debug('%s node classes discovered', len(self.node_classes))

        logger.debug('%s node stylesheets discovered',
                     len(self.node_stylesheets))

        logger.debug('%s node scripts discovered', len(self.node_scripts))

        # render html files
        logger.debug('rendering html files')

        # stylesheets
        self.style_tags_html: str = self.server.templating_engine.render_template(  # NOQA: LN001
            self.server.settings.STATIC_FILES_STYLE_TAGS_TEMPLATE,
            {
                'stylesheets': [i for i in self.node_stylesheets
                                if i.enabled and i.link],
            },
        )

        # scripts
        self.script_tags_html: str = self.server.templating_engine.render_template(  # NOQA: LN001
            self.server.settings.STATIC_FILES_SCRIPT_TAGS_TEMPLATE,
            {
                'scripts': [i for i in self.node_scripts
                            if i.enabled and i.link],
            },
        )

    def resolve_path(self, path: str) -> Optional[str]:
        logger.debug("resolving '%s'", path)

        rel_path = path

        if rel_path.startswith('/'):
            rel_path = rel_path[1:]

        # javascript client
        client_url = self.server.settings.STATIC_FILES_CLIENT_URL

        if client_url.startswith('/'):
            client_url = client_url[1:]

        if rel_path == client_url:
            logger.debug('returning javascript client')

            return self.server.client_pre_compiler.resolve()

        # searching in static dirs
        for static_dir in self.static_dirs:
            abs_path = os.path.join(static_dir, rel_path)

            logger.debug("trying '%s'", abs_path)

            if os.path.exists(abs_path):
                if os.path.isdir(abs_path):
                    logger.debug(
                        "'%s' is directory. resolving stopped", abs_path)

                    return None

                logger.debug("returning '%s'", abs_path)

                return abs_path

        # searching in node static files
        for static_file in self.static_files:
            if not static_file.enabled:
                continue

            if static_file.url == path:
                return static_file.path

        logger.debug("'%s' was not found", path)

        return None
