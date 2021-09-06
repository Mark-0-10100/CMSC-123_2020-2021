from django.shortcuts import render
from .models import Blogs

# A function that renders the "blogs" page
def blogs_view(request, *args, **kwargs):
    queryset = Blogs.objects.all()
    context = {
        "blogInDB":queryset
    }
    return render(request, "blogs.html", context)

#This functiion is for the content of the blogs
def blogsCONTENT_view(request, my_id):
    blogContent = Blogs.objects.get(id=my_id)
    context = {
        "title":blogContent.title,
        "description":blogContent.description
    }
    return render(request, "blogs_content.html", context)

def searchResults_view(request):
    if request.method == "POST":
        searchField = request.POST['searchField']
        blogSearch = Blogs.objects.filter(title__contains=searchField)
        context = {"searchField": searchField,
                    "blogSearch": blogSearch,
        }
        return render(request, "blogs_searchResults.html", context)