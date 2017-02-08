from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(object):

	def __init__(self, get_response):
		self.get_response = get_response
		print "middleware initiating"

	def __call__(self, request):
		response = self.get_response(request)
		print response
		print "middleware calling"
		return response

class BookMiddleware(MiddlewareMixin):
	def process_request(self, request):
		print "Middleware executed"
		print request.user
