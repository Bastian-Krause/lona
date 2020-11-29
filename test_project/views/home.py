def home(request):
    return """
        <h1>Lona Test Project</h1>

        <h2>View Types</h2>
        <ul>
            <li><a href="/view-types/interactive-view/">Interactive View</a></li>
            <li><a href="/view-types/non-interactive-view/">Non-Interactive View</a></li>
            <li><a href="/view-types/http-pass-through/">HTTP Pass Through View</a></li>
            <li><a href="/view-types/multi-user-view/">Multi User View</a></li>
            <li><a href="/view-types/daemonized-view/">Daemonized View</a></li>
            <li><a href="/view-types/class-based-view/">Class Based View</a></li>
        </ul>

        <h2>Response Types</h2>
        <ul>
            <li><a href="/response-types/template-response/">Template Response</a></li>
            <li><a href="/response-types/file-response/">File Response</a></li>
            <li><a href="/response-types/json-response/">JSON Response</a></li>
            <li><a href="/response-types/redirect/">Redirect</a></li>
            <li><a href="/response-types/http-redirect/">HTTP Redirect</a></li>
        </ul>

        <h2>Error Types</h2>
        <ul>
            <li><a href="/error-types/404/">Interactive 404</a></li>
            <li><a href="/error-types/404/" class="lona-ignore">Non Interactive 404</a></li>
            <li><a href="/error-types/interactive-500/">Interactive 500</a></li>
            <li><a href="/error-types/non-interactive-500/" class="lona-ignore">Non Interactive 500</a></li>
            <li><a href="/error-types/non-interactive-feature-error/">Non Interactive Feature Error</a></li>
        </ul>

        <h2>Routing</h2>
        <ul>
            <li><a href="/routing/url-args/foo/bar/baz/">URL Arguments</a></li>
            <li><a href="/routing/callback-view/">Callback View</a></li>
            <li><a href="/routing/http-pass-through-callback-view/">HTTP Pass Through Callback View</a></li>
        </ul>

        <h2>Events</h2>
        <ul>
            <li><a href="/events/click-events/">Click Events</a></li>
            <li><a href="/events/change-events/">Change Events</a></li>
            <li><a href="/events/non-node-events/">Non-Node Events</a></li>
            <li><a href="/events/widget-event-handler/">Widget Event Handler</a></li>
            <li><a href="/events/class-based-view/">Class Based View</a></li>
            <li><a href="/events/locking/">Locking</a></li>
        </ul>

        <h2>Forms</h2>
        <ul>
            <li><a href="/forms/interactive-form/">Interactive Form</a></li>
            <li><a href="/forms/non-interactive-form/">Non-Interactive Form</a></li>
        </ul>

        <h2>Window Actions</h2>
        <ul>
            <li><a href="/window-actions/set-title/">Set Title</a></li>
        </ul>
    """  # NOQA