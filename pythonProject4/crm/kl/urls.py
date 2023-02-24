from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,),
    path('compani', views.compani, name = 'compani'),
    path('kanban', views.kanban, name = 'kanban'),
    path('events', views.events, name = 'events'),
    path('customers', views.customers, name = 'customers'),
    path('service', views.service, name = 'service'),
    path('cash', views.cash, name = 'cash'),
    path('recruiting', views.recruiting, name = 'recruiting'),
    path('newcompani', views.newcompani, name = 'newcompani'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)