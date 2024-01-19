from lona_picocss import install_picocss

from schmona.html import HTML, H1, P
from schmona import View, App

app = App(__file__)

install_picocss(app, debug=True)


@app.route('/')
class Index(View):
    def handle_request(self, request):
        return HTML(
            H1('Hello World'),
            P('Lorem Ipsum'),
        )


app.run()
