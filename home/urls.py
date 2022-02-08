from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'
 
urlpatterns = [

    path('', views.index_, name='index_' ),
    path('<int:id>', views.End_sub, name='End_sub'),

   



   # path('<str:slug>', views.job_detail, name='job_detail'),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

