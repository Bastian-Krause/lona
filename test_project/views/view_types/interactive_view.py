from schmona.html import Strong, Select, HTML, Div, H2, Br
from schmona.view import View


class InteractiveView(View):
    def handle_request(self, request):
        widget = HTML()

        interval = Select(
            values=[
                (1,    '1s',    False),
                (0.5,  '0.5s',  True),
                (0.25, '0.25s', False),
                (0.01, '0.01s', False),
            ],
        )

        html = HTML(
            H2('Interactive View'),

            Strong('Interval: '),
            interval,
            Br(),
            Br(),

            widget,
        )

        while True:
            widget.clear()

            for i in range(0, 5):
                widget.append(Div(f'Div {i+1}'))
                self.show(html)

                self.sleep(float(interval.value))

            for i in range(0, 5):
                widget[i].insert(i+1, Div(f'Div {i+1}.{i+1}'))
                self.show(html)

                self.sleep(float(interval.value))

            for i in range(0, 5):
                widget[i].style = {'color': 'red'}
                self.show(html)

                self.sleep(float(interval.value))

            moving_div = Div('Div 6', style={'color': 'blue'})

            for i in range(0, 5):
                widget[i].append(moving_div)
                self.show(html)

                self.sleep(float(interval.value))

            self.show(html)
