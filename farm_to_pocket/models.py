from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    type_of_user = models.CharField(max_length=2, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    level = models.IntegerField(null=True)
    location = models.CharField(max_length=50)
    nearest_town = models.CharField(max_length=50)

    @classmethod
    def requested_users(cls, user_type):
        '''
        Method that gets list of farmers for buyer and vice versa
        '''
        if user_type == '1':
            requested_type = '2'
        else:
            requested_type = '1'

        found_users = User.objects.filter(type_of_user=requested_type)
        return found_users
# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    level = models.IntegerField(null=True)
    location = models.CharField(max_length=50)
    nearest_town = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50,null=True)
    availability = models.CharField(max_length=50)

class Seller(models.Model):
    name = models.CharField(max_length=30, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    level = models.IntegerField(null=True)
    location = models.CharField(max_length=50)
    nearest_town = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    seller = models.ForeignKey(Seller)
    availability = models.CharField(max_length=50)



class session_levels(models.Model):
	  session_id = models.CharField(max_length=25,primary_key=True)
	  phonenumber= models.CharField(max_length=25,null=True)
	  level = models.IntegerField(null=True)
