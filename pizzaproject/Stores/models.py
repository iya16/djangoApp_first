from re import RegexFlag
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class pizzeria(models.Model):
    pizzaria_name=models.CharField(max_length=200,blank=False)
    street=models.CharField(max_length=400, blank=True)
    city=models.CharField(max_length=400, blank=True)
    state=models.CharField(max_length=2, null=True, blank=True)
    zip_code=models.IntegerField(blank=True, default=0)
    website=models.URLField(max_length=420, blank=True)
    # phone_number=models.CharField(validators=[RegexValidator(RegexFlag==r'^\1?\d{9,10}$')], max_length=10, blank=True)
    phone_number = models.CharField(validators=[RegexValidator(r'^\d{9,10}$')],max_length=10,blank=True)
    description=models.TextField(blank=True)
    logo_image=models.ImageField(upload_to='pizzariaImage', blank=True)
    email=models.EmailField(max_length=254, blank=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return "{}, {}".format(self.pizzaria_name,self.city)
    
# phone_number = models.CharField(
    # validators=[RegexValidator(r'^\d{9,10}$')],
    # max_length=10,
    # blank=True
# )