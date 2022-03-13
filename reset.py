from django.contrib.auth.models import User

for o in User.objects.filter():
    o.delete()
