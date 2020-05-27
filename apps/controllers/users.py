from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class usercontroller:

    @staticmethod
    @login_required
    def index(request):
        template_name_index = 'users/index.html'
        return render(request, template_name=template_name_index)

    @staticmethod
    @login_required
    def detail(request, user_id):
        template_name_detail = 'users/detail.html'
        context = {'context_detail': "Thông tin detail " + str(user_id)}
        return render(request, template_name=template_name_detail, context=context)
