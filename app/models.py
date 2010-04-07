from django.db import models
#from django.contrib.auth.models import User, Permission

# Create your models here.
class Example(models.Model):
    #id is auto-defined and is auto-incrementing
    test = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.id
