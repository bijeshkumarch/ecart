from django.db import models

# Create your models here.

class Product(models.Model):
    produtc_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(default="", upload_to="shop/images")

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10, default='Not provided')
    cost = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.order_id) + "_" + self.name
    
class orderUpdate(models.Model):
    order_id = models.IntegerField(default='')
    update_id = models.AutoField(primary_key=True)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:14] + "..."