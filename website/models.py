from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering=['created_date']
    def __str__(self):
        return self.name



class NewsLetter(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email
