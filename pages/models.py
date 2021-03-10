from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Client(models.Model):
    """Model definition for Client."""
    client = models.CharField(verbose_name="Company Name", max_length=120, null=False, blank=False)
    website = models.URLField(max_length=200)
    logo = models.ImageField(upload_to="clients")
    class Meta:
        """Meta definition for Client."""
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        return self.client


    def get_absolute_url(self):
        """Return absolute url for Client."""
        return ('')

class ProjectCategory(models.Model):
    category = models.CharField(null=False,blank=False,max_length=120)
    
    class Meta:
        """Meta definition for Client."""
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'


    def __str__(self):
        return self.category
    


class Project(models.Model):
    project = models.CharField(verbose_name='Project name',max_length=120,null=False, blank=False)
    cover = models.ImageField(upload_to='blog/cover',help_text="dimensions are width is 1800 height is 1353 pixel") 
    task = models.CharField(verbose_name="Task", max_length=50,null=True)
    location = models.CharField(verbose_name="Location", max_length=50,null=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE,null=True)
    content = RichTextUploadingField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,max_length=150,blank=True,null=False)
    published = models.DateTimeField(verbose_name="published date", auto_now=False, auto_now_add=False, default=timezone.now())
    # FIELDNAME = models.DateField(verbose_name="Published", auto_now=True, auto_now_add=False)
    feautered = models.BooleanField(default=False)

    def __str__(self):
        return self.project

    def save(self):
        self.slug = slugify(self.project)
        super(Project, self).save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('pages:workdetail', kwargs={'slug': self.slug})


class ProjectStats(models.Model):
    project = models.ForeignKey(Project, verbose_name="project", on_delete=models.CASCADE)
    result = models.CharField(verbose_name="About Stats", max_length=80)
    number = models.IntegerField()

    def __str__(self):
        return self.result

    class Meta:
        """Meta definition for Client."""
        verbose_name = 'Project Stat'
        verbose_name_plural = 'Project Stats'