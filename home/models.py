from django.db import models

# Create your models here.


class Contact(models.Model):
    seriel_number = models.IntegerField(primary_key=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email_id = models.CharField(max_length=20)
    state = models.CharField(max_length=20,default='')
    city = models.CharField(max_length=20,default='')
    desc = models.CharField(max_length=500,default='')
    contact_number = models.IntegerField(max_length=14,default='')
    time = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'message from ' +  self.first_name + ' ' + self.last_name