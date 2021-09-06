"""webProject_sprint3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from homepage.views import homepage_view
from contactMe.views import contactMe_view
from projPortfolio.views import projPorfolio_view
from blogs.views import blogs_view, blogsCONTENT_view, searchResults_view

#urls for each of the page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',homepage_view),
    path('contactMe/', contactMe_view),
    path('portfolio/', projPorfolio_view),
    path('blogs/', blogs_view),
    path('blogs/<int:my_id>', blogsCONTENT_view),
    path('blogs/searchResult', searchResults_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)