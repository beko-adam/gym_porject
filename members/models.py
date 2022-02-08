from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

TYPE_JOB = (

            ('male', 'ذكر'),
            ('female', 'انثى'),

            )

TYPE_gruop = (

            ('الاولى', 'الاولى'),
            ('الثانية', 'الثانية'),
            ('الثالثه', 'الثالثه'),
            ('الرابعه', 'الرابعه'),
            ('الخامسه', 'الخامسه'),
            ('السادسه', 'السادسه'),
            ('السابعة', 'السابعة'),

            )

class Mumber(models.Model):
    owner = models.ForeignKey(User, related_name='ownr', on_delete=CASCADE)
    name = models.CharField(max_length=100)
    sex_type= models.CharField(max_length=15, choices=TYPE_JOB )
    gruop = models.TextField(max_length=10, choices=TYPE_gruop)
    published_at = models.DateField(auto_now=True)
    id_num = models.IntegerField(default=1)
    money = models.IntegerField(default=0)
    data_sub = models.DateField()
    phone = models.IntegerField(default=0)
    
   # category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField( upload_to='jobs',  default='default.jpg')
    
    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):

        return self.name