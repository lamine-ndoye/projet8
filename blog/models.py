from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.urls import reverse

from django.utils.text import slugify

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)


#formatage des caracteres
def __str__(self):
    return self.name


class article(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,related_name="category_posts"
        )
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    titel = models.CharField(max_length=25)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to= 'images',blank=True)
    description = models.CharField(max_length=255)
    details = models.CharField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,default='draft',max_length=10)
    publish = models.DateField(default=timezone.now)
    autors = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posted')
    objects = models.Manager() #manager par defaut
    published = PublishedManager() #custum manager
    
    
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.titel)
        super(article, self).save(*args, **kwargs)
   
   
    def __str__(self):
        return self.titel
    

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.details])
    
    
