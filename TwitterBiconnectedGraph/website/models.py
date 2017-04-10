from django.db import models

# Create your models here.
class TwitterUser(models.Model):
    name = models.CharField('name of Twitter user', max_length=50)

    class Meta:
        db_table = "twitter_user"

    def __str__(self):
        return self.name

a = TwitterUser(id=1, name='test')


a.save()