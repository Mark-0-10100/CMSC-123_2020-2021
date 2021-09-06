from django.contrib import admin
from .models import *

# Registers the models(objects in database)
admin.site.register(Portfolio_softProj)
admin.site.register(Portfolio_artProj)
admin.site.register(Portfolio_researchProj)
admin.site.register(Portfolio_progressProj)
admin.site.register(Portfolio_futureProj)