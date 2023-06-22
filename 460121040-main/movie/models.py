from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxLengthValidator,MinLengthValidator

class OtoTamir(models.Model):
 OtoTamir_ID = models.IntegerField(primary_key= True)
 Adres = models.CharField(max_length=250)
 Number = models.CharField(max_length=25)
 Mail = models.EmailField()

 def __str__(self):
        return self.Full_name
 
class Servis(models.Model):
 Servis_ID = models.IntegerField(primary_key= True)
 Name = models.CharField(max_length=50)


 
class Person(models.Model):
 Person_ID = models.IntegerField(primary_key= True)
 Full_name = models.CharField(max_length=250)
 Img = models.ImageField(upload_to='movie/images/'  ) 
 Brithday = models.DateField()
 Kayıt_date = models.DateField(auto_now=True)
 Number = models.CharField(max_length=250)
 Mail = models.EmailField()
 Servis_ID=models.ManyToManyField(Servis)
 


class Musteri(models.Model):
 Musteri_ID = models.IntegerField(primary_key= True)


class Adres(models.Model):
 Adres_ID = models.IntegerField(primary_key= True)
 il = models.CharField(max_length=50)
 ilce = models.CharField(max_length=50)
 mahalle_no = models.IntegerField()
 Musteri_ID=models.ForeignKey(Musteri,on_delete=models.CASCADE,null=True)
 Person_ID=models.ForeignKey(Person,on_delete=models.CASCADE,null=True)

class Car(models.Model):
 Car_ID = models.IntegerField(primary_key= True)
 Marka = models.CharField(max_length=250)
 Model = models.CharField(max_length=250)
 Yil = models.CharField(max_length=250)
 user =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
 
 def __str__(self):
        return self.Marka



class Testimonial(models.Model):
 Testimonial_ID = models.IntegerField(primary_key= True)
 Yorum = models.TextField(validators=[MinLengthValidator(10)])
 user =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
 


class Furnitures(models.Model):
 Furnitures_ID = models.IntegerField(primary_key= True)
 Aciklama = models.CharField(max_length=250)
 Img = models.ImageField(upload_to='movie/images/'  ) 
 Servis_ID=models.ForeignKey(Servis,on_delete=models.CASCADE,null=True)



class Contact_us(models.Model):
 Contact_us_ID = models.IntegerField(primary_key= True)
 Message = models.TextField(validators=[MinLengthValidator(10)])


class About(models.Model):
 About_ID = models.IntegerField(primary_key= True)
 Title = models.CharField(max_length=250)
 altbaslik = models.CharField(max_length=250)
 aciklama = models.TextField(validators=[MinLengthValidator(10)])
 OtoTamir_ID =models.OneToOneField(OtoTamir,on_delete=models.CASCADE,null=True,blank=True,)


 
class Home(models.Model):
 Home_ID=models.IntegerField(primary_key=True)
 Title = models.CharField(max_length=250)
 aciklama = models.TextField(validators=[MinLengthValidator(10)])
 Img = models.ImageField(upload_to='movie/images/'  ) 
 

 
class Rezervation(models.Model):
    full_name=models.CharField(max_length=50)
    telephone=models.IntegerField()
    email=models.EmailField(max_length=150)
    date=models.DateTimeField()
    
    description=models.CharField(max_length=500)
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def str(self):
         return self.full_name




# Create your models here.
