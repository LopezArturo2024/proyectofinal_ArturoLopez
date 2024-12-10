from django.http import HttpResponse

def prueba(request):
    return HttpResponse(f"Prueba")