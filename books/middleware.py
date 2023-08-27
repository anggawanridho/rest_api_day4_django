from django.http import JsonResponse

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            role = request.GET.get('role')
            if role != 'admin':
                return JsonResponse({'message': 'Access denied'}, status=403)
        response = self.get_response(request)
        return response