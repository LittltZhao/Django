from django.db import models
from django.contrib import admin
# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=20)
    body=models.TextField()
    tiemstamp=models.DateTimeField()
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','tiemstamp')




class Author(models.Model):
    name=models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author)
    length=models.IntegerField()
    def __unicode__(self):
        return self.title
class Authoring(models.Model):
    co=models.CharField(max_length=100)
    book=models.ForeignKey(Book)
    author=models.ForeignKey(Author)
    def __unicode__(self):
        return self.co
class SmithBook(Book):
    authorname=models.ManyToManyField(Author)


admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Authoring)
admin.site.register(SmithBook)

