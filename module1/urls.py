from django.contrib import admin
from django.urls import path
from.views import*

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console, name = 'print_to_console'),
    path('p/',print1, name = 'print1'),
    path('ran1/', ran, name='ran'),
    path('ran/', random123, name='random123'),
    path('d/',get_date,name='get_date'),
    path('dt/',getdate1,name='getdate1'),
    path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    path('db/',dataconnection,name='dataconnection'),
    path('dbc/',registerloginfunction,name='registerloginfunction'),
    path('pie1/',pie_chart,name='pie_chart'),
    path('slide/',slidefun,name='slidefun'),
    path('w/',weathercall,name="weathercall"),
    path('w2/',weatherlogic,name="weatherlogic"),
    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path('login1/',login1,name='login1'),
    path('signup1/',signup,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contact/',contact,name='contact'),
    path('contactmail/',contactmail,name='contactmail'),
]