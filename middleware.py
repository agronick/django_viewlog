from models import PageLog


class ViewCountMiddleware(object):

    ingore_contains = ['static' ,'admin']

    def log_view_on_close(self):
        ret = super(self.response.__class__, self.response).close()
 
	if not len([i for i in self.ingore_contains if i in self.request.path]): 
		view_log = PageLog()
		view_log.user = self.request.user if self.request.user.is_authenticated() else None
		view_log.path = self.request.path
		view_log.request_type = self.request.method
		view_log.referrer = self.request.META.get('HTTP_REFERER','')
		view_log.browser = self.request.META.get('HTTP_USER_AGENT','')
		view_log.status_code = self.response.status_code
		view_log.save()

        return ret
    
    def process_response(self, request, response):
        self.request = request
        self.response = response
 
        response.close = self.log_view_on_close
        return response
