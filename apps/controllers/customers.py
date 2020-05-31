from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from databases.postgresqldb import postgresqldb
from django.core.paginator import Paginator
from utils.constants import const_common
from utils.urlhelpers import urlhelper


class customerindex(View):
    template_name = 'customers/index.html'

    def get(self, request):
        _db = postgresqldb()
        _datas = _db.getcustomerdatas()
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
        print(kwargs)
        print(request.META.get('HTTP_REFERER', '/'))
        print(request.path_info)
        print(request.build_absolute_uri())
        print(request.get_full_path())
        _url_index = urlhelper.get_url_refer(request, '/customer/index')
        cus_id = kwargs["slug"]
        context = {'context_edit': "Thông tin Sửa customer " + str(cus_id), 'url_index': _url_index}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.POST.get('EMAIL', ''))
        print(request.META.get('HTTP_REFERER', '/'))
        print(request.path_info)
        print(request.build_absolute_uri())
        print(request.get_full_path())

        _url_index = request.POST.get('URL_INDEX', '/customer/index')
        print(_url_index)
        # return redirect(to=_url_index)
        return HttpResponseRedirect(redirect_to=_url_index)


class customerdelete(View):

    def get(self, request, *args, **kwargs):
        print(kwargs)
        cus_id = kwargs["cus_id"]
        print("username: {}".format(cus_id))
        # base_url = reverse('apps1:customer_index')  # 1 /products/
        # query_string = urlencode({'page': 2})  # 2 category=42
        # url = '{}?{}'.format(base_url, query_string)  # 3 /products/?category=42
        _url_index = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(_url_index)
