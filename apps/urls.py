# from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from apps.controllers import users, customers

# urlpatterns = [
#     url(r'^aaa$', users.index(), name='user_index')
# ]
app_name = 'apps1'
urlpatterns = [
    path('user/index', users.usercontroller.index, name='user_index'),
    path('user/detail/<str:user_id>', users.usercontroller.detail, name='user_detail'),
    path('customer/index', customers.customerindex.as_view(), name='customer_index'),
    path('customer/create', customers.customercreate.as_view(), name='customer_create'),
    path(r'customer/edit/<str:cus_id>', customers.customeredit.as_view(), name='customer_edit')
]
