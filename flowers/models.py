from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Flowers(models.Model):
    name_f=models.CharField(max_length=50)
    description=models.TextField()
    image_flower=models.ImageField(default='flower_image/flower_default_image.jpg',upload_to='media/')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    symbolism=models.CharField(max_length=50,blank=True,null=True)
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.name_f

    class Meta:
        db_table='flower_table'


class Designer(models.Model):
    name=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table='designer_table'


class FlowerDesigner(models.Model):
    flower=models.ForeignKey(Flowers,on_delete=models.CASCADE)
    designer=models.ForeignKey(Designer,on_delete=models.CASCADE)


    def __str__(self):
        return  f'{self.flower.name_f}  {self.designer.name}'

    def get_info(self):
        return  f'{self.flower.name_f}  {self.designer.name}'

    class Meta:
        db_table='flower_designer_table'


class FlowerReview(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    flower=models.ForeignKey(Flowers,on_delete=models.CASCADE,related_name='flower_review')
    comment=models.TextField()
    star_given=models.PositiveIntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table='review_table'

    def __str__(self):
        return self.flower.name_f