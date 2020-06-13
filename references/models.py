from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(statusRf='published')

class References (models.Model) : 
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    titleRf = models.CharField(max_length=250)
    descriptionRf = models.TextField()
    linkRf = models.URLField()
    authorRf = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'references_posts')
    createdRf = models.DateTimeField(auto_now_add=False) 
    updatedRf = models.DateTimeField(auto_now=False)
    publish = models.DateTimeField(default=timezone.now)
    statusRf = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ('-titleRf',)

    def __str__(self):
        return self.titleRf
    
    def get_absolute_url(self):
        return reverse("references:references_detail", 
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.titleRf])

