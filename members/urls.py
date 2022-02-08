from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'members'
 
urlpatterns = [

    path('', views.all_members, name='all_members' ),
    path('add', views.Add_mumber, name='Add_mumber' ),

    path('<int:id>', views.detalis_members, name='detalis_members'),
    path('<int:id>edit', views.Editr_Mumber, name='Editr_Mumber'),
    path('<int:id>edit_sub', views.Editr_Mumber_usb, name='Editr_Mumber_usb'),



   # path('<str:slug>', views.job_detail, name='job_detail'),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

