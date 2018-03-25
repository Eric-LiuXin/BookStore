from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    create_date = models.DateField(auto_now=True)
    intro = models.TextField(max_length=200)
    down_link = models.CharField(max_length=200)

    class Meta:
        ordering = ('-create_date',)

    def __unicode__(self):
       return self.name