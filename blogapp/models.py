from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect
# from . import views
# Create your models here.
STATUS=((0,'Drafts'),(1,'Published'))

class Post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_Post')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    status=models.IntegerField(choices=STATUS,default=0)

    class Meta:
        ordering=['-created_on']
#         permissions=(
#             ("can_add_data","can add a new data"),
#         )
# if request.user.has_perm('blogapp.can_add_data'):
#     model= Post
#     template_name=("http://127.0.0.1:8000/admin/blogapp/post/add/")
# else:
#     model=Post
#     template_name=("http://127.0.0.1:8000/")
def __str__(self):
        return self.title