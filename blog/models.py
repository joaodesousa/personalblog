from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"Rascunho"),
    (1,"Publicado")
)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length= 75, verbose_name="Título")
    byline = models.CharField(max_length=75, verbose_name="Subtítulo")
    text = models.TextField(verbose_name="Corpo")
    image = models.ImageField(upload_to='post', blank= True, null=True, verbose_name="Imagem")
    slug = models.SlugField(max_length=128, verbose_name="URL")
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return "%s" % (self.title)
