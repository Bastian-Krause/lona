from datetime import datetime

from schmona.html import Strong, Button, Span, Div, H2, Br
from schmona.view import View


class LockingView(View):
    def handle_request(self, request):
        now = Span()
        self.message = Div('Button not clicked')
        self.button = Button('Button')

        self.html = Div(
            H2('HTML Tree Locking View'),
            Div(Strong('Now: '), now),
            Br(),
            self.message,
            self.button,
        )

        while True:
            now.set_text(datetime.now())
            self.show(self.html)

            self.sleep(1)

    def handle_input_event(self, input_event):
        with self.html.lock:
            self.message.set_text('Button clicked; Lock')
            self.show(self.html)

            self.sleep(2)

            self.message.set_text('Unlock')
            self.show(self.html)
