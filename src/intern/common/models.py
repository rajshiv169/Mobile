from django.db import models

class Mobile(models.Model):
    model_name = models.CharField(max_length=10)
    company_name = models.CharField(max_length=10)
    price = models.IntegerField()
    os = models.CharField(max_length=10)
    processor = models.CharField(max_length=20)
    data_transfer = models.IntegerField()
    processor_speed = models.IntegerField()

    def __str__(self):
        return self.model_name
    
    def get_absolute_url(self):
        return reverse("details", kwargs={"id":self.id})

