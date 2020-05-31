from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import urlencode
from django.views import View
from databases.postgresqldb import postgresqldb
from django.core.paginator import Paginator
from utils.constants import const_common
from utils.urlhelpers import urlhelper


class authlogin(View):
    template_name = 'auths/login.html'

    def get(self, request, *args, **kwargs):
        context = {'context_create': "Thông tin login : BẠN PHẢI ĐĂNG NHẬP!"}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        pass