import re


class urlhelper:

    @staticmethod
    def get_url_refer(request, default=None):
        if not request.META.get('HTTP_REFERER'):
            return default
        return request.META.get('HTTP_REFERER')

    @staticmethod
    def get_referer_view(request, default=None):
        '''
        Return the referer view of the current request

        Example:

            def some_view(request):
                ...
                referer_view = get_referer_view(request)
                return HttpResponseRedirect(referer_view, '/accounts/login/')
        '''

        # if the user typed the url directly in the browser's address bar
        referer = request.META.get('HTTP_REFERER')
        if not referer:
            return default

        # remove the protocol and split the url at the slashes
        referer = re.sub('^https?:\/\/', '', referer).split('/')
        if referer[0] != request.META.get('SERVER_NAME'):
            return default

        # add the slash at the relative path's view and finished
        referer = u'/' + u'/'.join(referer[1:])
        return referer
