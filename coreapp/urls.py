from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'Wisfrags Education Private Limited - BlissedMaths SuperAdmin Panel'
admin.site.site_title = 'Wisfrags Education'
admin.site.index_title = 'Managed by Gaurav Malhotra, Pankaj Kumar & Ishwar Jangid'

# from knox import views as knox_views
from django.urls import path
from coreapp.views import *

urlpatterns = [


    path('validate_phone/',ValidatePhoneSendOTP.as_view()),
    path('login/',LoginAPI.as_view()),
    path('validate-otp/',ValidateOTP.as_view()),
    # path('logout/',knox_views.LogoutView()),
    path('register/',Register.as_view()),
    re_path(r'^admin/', admin.site.urls),
    
    

   
]



if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)