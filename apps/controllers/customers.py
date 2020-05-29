from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from databases.postgresqldb import postgresqldb
from django.core.paginator import Paginator
from utils.constants import const_common


class customerindex(View):
    template_name = 'customers/index.html'

    def get(self, request):
        _db = postgresqldb()
        _datas = _db.getdatas()
        _paginator = Paginator(_datas, const_common.PAGE_SIZE)
        _page = request.GET.get('page')
        _items = _paginator.get_page(_page)
        _context = {'items': _items}
        return render(request, self.template_name, context=_context)


class customercreate(View):
    template_name = 'customers/create.html'

    def get(self, request, *args, **kwargs):
        context = {'context_create': "Thông tin Tạo mới customer"}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        pass


class customeredit(View):
    template_name = 'customers/edit.html'

    def get(self, request, *args, **kwargs):
        cus_id = request.GET.get('cus_id', '')
        cus_name = request.GET.get('cus_name', '')
        context = {'context_edit': "Thông tin Sửa customer " + str(cus_id) + " name: {}".format(cus_name)}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        pass
