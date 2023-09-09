from django.shortcuts import render
from django.views import generic, View

# Create your views here.


# def index(request):
#     """Index page view """
#     return render(request, 'index.html')


class Home(generic.TemplateView):
    """
    View to display the home page
    """
    template_name = "index.html"
