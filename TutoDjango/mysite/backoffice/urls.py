from django.conf.urls import include, url
from . import views
from backoffice.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = (
    url(r'^$', views.home, name='home'),
    url(r'^$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^backoffice/$', login_required(TemplateView.as_view(template_name='backoffice/index.html'))),
)