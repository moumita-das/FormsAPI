from api import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.create_view), # root
    url(r'^login$', views.login_view,name="login"), # login
    url(r'^logout$', views.logout_view,name="logout"), # logout
    url('api-fetch',views.retrieveView,name="api-fetch"),
]
