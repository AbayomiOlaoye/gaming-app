from django.http import HttpResponse
from django.template import loader

# Create your views here.
def gamers(request):
    temp = loader.get_template('players.html')
    return HttpResponse(temp.render())
