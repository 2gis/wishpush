# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from dashboard.models import Wish, WishForm

message_to_pusher = u"""
Дорогой друг,

Мы получили от тебя желание:
{wish}

Мы постараемся сделать все возможное, чтобы как можно скорее исполнить твою хотелку. Как только мы возьмем ее в работу, тебе на почту придет письмо. Также ты можешь отследить статус своего желания на нашем сервисе http://ссылка

Твоя команда автоматизации
""".encode('utf-8')

message_to_autoqa = u"""
Поступило новое желание:
{wish}

от {email}
""".encode('utf-8')

def send_mails(email, wish):
	from django.core.mail import send_mail
	
	# send_mail(
	# 	"Your wish is our wish!",
	# 	message_to_pusher.format(wish=wish),
	# 	"autoqa@2gis.ru",
	# 	[email]
	# )

	send_mail(
		"New wish",
		message_to_autoqa.format(email=email,wish=wish),
		"wishpushnotifier@gmail.com",
		["i.pavlov@2gis.ru"]
	)

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

			send_mails(email, wish)

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