from django.db import models

class contactus(models.Model):
    username=models.CharField( max_length=50)
    useremail =models.EmailField(max_length=254)
    phonenumber=models.IntegerField()
    massage=models.TextField()

    myimages = models.ImageField(upload_to="images", null=True, blank=True)


# Create your models here.
