# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from dashboard.models import Wish, WishForm

def index(request):
	wish_list = Wish.objects.order_by('date')[:5]
	
	if request.method == 'POST': # If the form has been submitted...
		form = WishForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			email = form.cleaned_data['email']
			wish = form.cleaned_data['wish']

			from django.utils import timezone
			w = Wish(email=email, wish=wish, date=timezone.now())
			w.save()
			# from django.core.mail import send_mail
			# send_mail("Your wish is our wish!", wish + "\n\nNow we know, thanks!", "autoqa@2gis.ru", [email])
			return HttpResponseRedirect('/dashboard/') # Redirect after POST
		else:
			context = {
				'form': form,
				'wish_list': wish_list,
			}
		return render(request, 'dashboard/index.html', context)
			
		#return HttpResponse("there's an error")
	else:
		form = WishForm() # An unbound form
		context = {
			'form': form,
			'wish_list': wish_list,
		}
		return render(request, 'dashboard/index.html', context)

def thanks(request):
	pass