from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from databases.postgresqldb import postgresqldb
from django.core.paginator import Paginator
from utils.constants import const_common

class usercontroller:

    @staticmethod
    #@login_required
    def index(request):
        template_name_index = 'users/index.html'
        _db = postgresqldb()
        _datas = _db.getdatas()
        _paginator = Paginator(_datas, const_common.PAGE_SIZE)
        _page = request.GET.get('page')
        _items = _paginator.get_page(_page)
        _context = {'items': _items}
        return render(request, template_name=template_name_index, context=_context)

    @staticmethod
    #@login_required
    def detail(request, user_id):
        template_name_detail = 'users/detail.html'
        context = {'context_detail': "Thông tin detail " + str(user_id)}
        return render(request, template_name=template_name_detail, context=context)
