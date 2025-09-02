
from django.contrib import admin
from django.urls import path
from produtos.views import lista_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', lista_produtos),
]
