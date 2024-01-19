from schmona.view import View


class NonNodeEventView(View):
    def handle_request(self, request):
        template = """
            <h2>Non-Node Events</h2>
            <div>{}</div>
            <button id="red-button" data-lona-events="301" style="color: white; background-color: red;">Red Button</button>
            <button id="green-button" data-lona-events="301" style="color: white; background-color: green;">Green Button</button>

        """  # NOQA: LN002

        message = 'No button pressed'

        while True:
            html = template.format(message)

            input_event = self.await_input_event(html=html)

            if input_event.node_has_id('red-button'):
                message = 'Red Button clicked'

            elif input_event.node_has_id('green-button'):
                message = 'Green Button clicked'

            else:
                message = 'Error: unknown event issuer'
