from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [

    path(route='', view=views.get_dealerships, name='index'),
    path(route='about', view=views.get_about, name='about us'),
    path(route='contact',view=views.get_contact, name='contact us'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='login', view=views.login_request,name='login'),
    path(route='signup',view=views.registration_request,name='signup')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
