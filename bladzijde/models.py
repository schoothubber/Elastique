from django.db import models

# Create models for:

#Publishers; id, name
#Authors; id, first_name, last_name
#books;id, title, description, cover_url, isbn, publisher, author




class Publishers(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Authors(models.Model):
    number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        full_name = "%s %s"%(self.first_name, self.last_name)
        return full_name

class Books(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    cover_url = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publishers, on_delete = models.CASCADE, null = True)
    author = models.ForeignKey(Authors, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.title
