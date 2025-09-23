from django.views import View as views
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(views):
    def get(self, request):
        return HttpResponse('Hello, World!')