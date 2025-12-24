from django.db import models


class Project(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='static/images/project_images', default='static/images/my_logo.png')
    title = models.CharField(max_length=255)
    github_link = models.URLField(unique=True)
    site_url = models.URLField(unique=True, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='static/images/project_images', default='static/images/my_logo.png')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)
    