wishpush
========

Service for pushing wishes to jira

# install
+ git clone ...
+ cd wishpush
+ python manage.py syncdb
+ python manage.py sql dashboard
+ python manage.py syncdb
+ python manage.py collectstatic

# run
+ python manage.py runserver 0.0.0.0:8081

# to add a wish to debug:

+ python manage.py shell
+ from dashboard.models import Wish
+ from django.utils import timezone
+ w = Wish(email="test@test.ru", wish="help me!", date=timezone.now())
+ w.save()
+ Wish.objects.all()