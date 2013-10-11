# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from dashboard.models import Wish

def index(request):
	wish_list = Wish.objects.order_by('date')[:5]
	# template = loader.get_template('dashboard/index.html')
	# context = RequestContext(request, {
	#     'wish_list': wish_list,
	# })
	context = {
		'wish_list': wish_list,
	}
	return render(request, 'dashboard/index.html', context)
    # return HttpResponse(template.render(context))