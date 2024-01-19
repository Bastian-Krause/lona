from schmona.errors import ForbiddenError
from schmona.view import View


class DenyAccess(View):
    def handle_request(self, request):
        raise ForbiddenError()
