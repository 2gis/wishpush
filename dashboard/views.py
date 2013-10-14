# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from dashboard.models import Wish, WishForm
from notifier.models import Notifier

def index(request):
	wish_list = Wish.objects.order_by('-date')[:]
	
	if request.method == 'POST': # If the form has been submitted...
		form = WishForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			email = form.cleaned_data['email']
			wish = form.cleaned_data['wish']

			from django.utils import timezone
			w = Wish(email=email, wish=wish, date=timezone.now())
			w.save()

			notifier = Notifier()
			notifier.send_emails(email, wish)
			notifier.voice_notify("Поступило новое желание от {name}".format(name=email))

			return HttpResponseRedirect('/dashboard/') # Redirect after POST
		else:
			context = {
				'form': form,
				'wish_list': wish_list,
			}
		return render(request, 'dashboard/index.html', context)
	else:
		form = WishForm() # An unbound form
		context = {
			'form': form,
			'wish_list': wish_list,
		}
		return render(request, 'dashboard/index.html', context)

def thanks(request):
	pass