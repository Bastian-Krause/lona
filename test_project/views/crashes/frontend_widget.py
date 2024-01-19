from schmona.static_files import Script
from schmona.html import Widget, HTML
from schmona.view import View


class CrashingFrontendWidget(Widget):
    STATIC_FILES = [
        Script(
            name='CrashingFrontendWidget',
            path='crashing_frontend_widget.js',
        ),
    ]

    FRONTEND_WIDGET_CLASS = 'crashing_frontend_widget'


class CrashingFrontendWidgetView(View):
    def handle_request(self, request):
        html = HTML(
            CrashingFrontendWidget(),
        )

        self.show(html)
