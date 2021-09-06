from django.shortcuts import render
from .models import *

# A function that renders the "Project portfolio" page
def projPorfolio_view(request, *args, **kwargs):
     context = {}
     return render(request, "projectPortfolio.html", {})

