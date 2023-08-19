from django.db import models

# Create your models here.
class Details(models.Model):
    d_name = models.CharField(max_length=20)
    d_age = models.IntegerField()
    d_skills = models.CharField(max_length=20)
    d_desgination = models.CharField(max_length=20)
    d_address = models.CharField(max_length=20)
    
    def __str__ (self):
        return self.d_name
    


    # def __str__ (self):
        # return self.d_skills
    # def __str__ (self):
        # return self.d_desgination
    # def __str__(self):
        # return self.d_address

    