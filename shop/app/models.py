from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('CR', 'Crud'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Panner'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

STATE_CHOICES = (
    ('Assam', 'Assam'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
)
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    product_image = models.ImageField(upload_to = "product")

    def _str_(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    mobile = models.IntegerField(default = 0)
    zipcode  = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length = 100)
    
    def __str__(self):
        return self.name