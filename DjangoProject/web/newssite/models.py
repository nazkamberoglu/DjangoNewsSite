from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name

class News(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="images")

    class Meta:
        verbose_name_plural="News"

    def __str__(self):
        return self.title

class Horoscope(models.Model):
    sign = models.CharField(max_length=50)
    prediction = models.TextField()
    image = models.ImageField(upload_to='horoscope_images/', blank=True, null=True)


    def __str__(self):
        return self.sign


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)


    def __str__(self):
        return self.title