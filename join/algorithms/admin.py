from django.contrib import admin

# Register your models here.
from .models import Algo, PPLWhoHaveSolvedAlgo

admin.site.register(Algo)

admin.site.register(PPLWhoHaveSolvedAlgo)
