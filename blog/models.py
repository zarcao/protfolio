from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(default='标题',max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.png',upload_to='images/')
    text = models.TextField(default='啥都没写啊')

    def __str__(self):
        return self.title