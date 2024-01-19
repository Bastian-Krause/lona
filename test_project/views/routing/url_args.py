from schmona.view import View


class URLArgsView(View):
    def handle_request(self, request):
        return f"""
            <h2>URL Arguments</h2>
            <div>a={request.match_info['a']}</div>
            <div>b={request.match_info['b']}</div>
            <div>c={request.match_info['c']}</div>
        """
