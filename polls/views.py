from django.http import HttpResponse

def index(request):
    return HttpResponse("ITS A POLL APP")

# Create your views here.
