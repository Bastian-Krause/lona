from datetime import datetime

from schmona.html import HTML, H2
from schmona._json import dumps
from schmona.view import View


class CustomMessagesView(View):
    def handle_request(self, request):
        html = HTML(
            H2('Messages'),
        )

        self.show(html)

        while True:
            private_message = dumps({
                'notification': {
                    'message': f'{datetime.now()}: This is a message',
                    'timeout': 2000,
                },
            })

            broadcast_message = dumps({
                'notification': {
                    'message': f'{datetime.now()}: This is a broadcast message',
                    'timeout': 2000,
                },
            })

            self.send_str(private_message)
            self.send_str(broadcast_message, broadcast=True)

            self.sleep(1)
