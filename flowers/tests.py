from django.test import TestCase
from django.urls import reverse

from .models import Flowers

# Create your tests here.

class FlowerListTest(TestCase):
    def test_flower_list(self):
        Flowers.objects.create(name_f='name_f1',price=12400,description='description1',symbolism='symbolism1')
        Flowers.objects.create(name_f='name_f2',price=12300,description='description2',symbolism='symbolism2')
        Flowers.objects.create(name_f='name_f3',price=44400,description='description3',symbolism='symbolism3')

        flowers = Flowers.objects.all()
        flower_list = self.client.get(reverse('flowers:flower-list'))
        # print(flower_list.content)  # Print the content of the response

        for flower in flowers:
            self.assertContains(flower_list,flower.name_f)


    def test_detail(self):
        flower=Flowers.objects.create(name_f='name_f2',price=12300,description='description2',symbolism='symbolism2')
        flower_detail=self.client.get(reverse('flowers:flower-detail',kwargs={'pk':flower.pk}))
        self.assertContains(flower_detail, flower.name_f)