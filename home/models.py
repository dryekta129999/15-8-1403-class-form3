from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS =(
        ('pub' , 'انتشار یافته'),
        ('drf' , 'پیش نمایش'),
    )
    title = models.CharField(max_length=50)
    information = models.TextField(max_length=500,null=True,blank=True)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS , max_length=3)

    def __str__(self):
        return self.title

