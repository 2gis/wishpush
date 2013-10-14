# -*- coding: utf-8 -*-
import httplib, urllib

from django.db import models
from django.conf import settings

class VoiceNotifier(object):
	_host = settings.VOICE_NOTIFIER_HOST
	_port = settings.VOICE_NOTIFIER_PORT
	_service = settings.VOICE_NOTIFIER_SERVICE
	
	_text = "Поступило новое желание"

	def notify(self, text):
		if not text:
			text = self._text
		conn = httplib.HTTPConnection(self._host, self._port)
		params = urllib.urlencode({'text': text})
		headers = {
			"Content-type": "text/plain",
		}
		conn.request("POST", self._service, params, headers)


class Notifier(object):
	_message_to_pusher = u"""
Дорогой друг,

Мы получили от тебя желание:
{wish}

Мы постараемся сделать все возможное, чтобы как можно скорее исполнить твою хотелку. Как только мы возьмем ее в работу, тебе на почту придет письмо. Также ты можешь отследить статус своего желания на нашем сервисе http://ссылка

Твоя команда автоматизации
""".encode('utf-8')

	_message_to_autoqa = u"""
Поступило новое желание:
{wish}

от {email}
""".encode('utf-8')

	def email_pusher(self, email, wish):
		subject = "Your wish is our wish"
		message = self._message_to_pusher.format(wish=wish)
		email_from = "autoqa@2gis.ru"

		from django.core.mail import send_mail
		send_mail(subject, message, email_from,	[email])

	def email_autoqa(self, email, wish):
		subject = "New wish"
		message = self._message_to_autoqa.format(email=email, wish=wish)
		email_from = "notifier@2gis.ru"

		from django.core.mail import send_mail
		send_mail(subject, message, email_from,	[email])

	def send_emails(self, email, wish):
		self.email_pusher(email,wish)
		self.email_autoqa(email,wish)

	def voice_notify(self, text):
		voice_notifier = VoiceNotifier()
		voice_notifier.notify(text)