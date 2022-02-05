from django.urls import path
from .import views


urlpatterns = [
  path('',views.home,name="home"),
  path('booths/',views.booth_list,name="both_list"),
  path('boothdetail/',views.booth_details,name="booth_detail"),
  path('login/',views.login_Password,name="login"),
  path('changestatus/',views.change_status,name="change_status"),
]