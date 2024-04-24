from django.db import models

# Create your models here. 

class Blogspot(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    head0_content = models.CharField(max_length=500, default="")
    head1 = models.CharField(max_length=500, default="")
    head1_content = models.CharField(max_length=500, default="")
    head2 = models.CharField(max_length=500, default="")
    head2_content = models.CharField(max_length=500, default="")
    pub_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.title