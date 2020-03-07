from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=40)
    dir = models.CharField(max_length=40) # Le plus souvent la même chose que le nom.

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class File(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    file = models.FileField(upload_to="static/media/files")
    date_publish = models.DateTimeField('date published')
    date_written = models.DateTimeField('date written')
    author = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.section.name + "/" + self.name
