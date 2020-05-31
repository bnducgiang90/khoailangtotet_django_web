# from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import TemplateView
from apps.controllers import users, customers, auths

# urlpatterns = [
#     url(r'^aaa$', users.index(), name='user_index')
# ]
app_name = 'apps1'
urlpatterns = [
    path('user/index', users.usercontroller.index, name='user_index'),
    path('user/detail/<str:user_id>', users.usercontroller.detail, name='user_detail'),
    path(r'customer/index', customers.customerindex.as_view(), name='customer_index'),
    path('customer/create', customers.customercreate.as_view(), name='customer_create'),
    re_path(r'^customer/edit/(?P<slug>[a-zA-Z0-9_.-]+)/$', customers.customeredit.as_view(), name='customer_edit'),
    path(r'customer/delete/<str:cus_id>', customers.customerdelete.as_view(), name='customer_delete'),
    path(r'auth/login', auths.authlogin.as_view(), name='auth_login'),
    path(r'auth/register', auths.authregister.as_view(), name='auth_register'),
    path(r'auth/logout', auths.authlogout.as_view(), name='auth_logout'),
]
