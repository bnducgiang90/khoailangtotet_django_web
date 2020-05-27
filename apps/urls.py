# from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from apps.controllers import users

# urlpatterns = [
#     url(r'^aaa$', users.index(), name='user_index')
# ]
app_name = 'apps1'
urlpatterns = [
    path('user/index', users.usercontroller.index, name='user_index'),
    path('user/detail/<str:user_id>', users.usercontroller.detail, name='user_detail')
]
