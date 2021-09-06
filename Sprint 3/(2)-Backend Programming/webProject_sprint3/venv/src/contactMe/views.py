from django.shortcuts import render
from .models import ContactMe
from .forms import ContactMe_Forms
from django.http import HttpResponse

# A function that renders the contact Me forms.
def contactMe_view(request):
    my_form = ContactMe_Forms() 
    if request.method == "POST": # When the user submits something
        my_form = ContactMe_Forms(request.POST)
        if my_form.is_valid():  #When form is valid and submitted
            ContactMe.objects.create(**my_form.cleaned_data)
            my_form = ContactMe_Forms()
    context = {
        "form":my_form 
    }

    return render(request, "contactMe.html", context)
