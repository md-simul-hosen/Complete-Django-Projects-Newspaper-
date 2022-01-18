from django.db import models


class info(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=15)
    con_password = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class products(models.Model):
    heading = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.heading

