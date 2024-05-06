from django.db import models

class FabricRoll(models.Model):
    number = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    weight_or_length = models.CharField(max_length=50)
    fabric_composition = models.CharField(max_length=50)
    arrival_date = models.DateField(auto_now_add=True)

class Cutting(models.Model):
    fabric_roll = models.ForeignKey(FabricRoll, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    model_name = models.CharField(max_length=100)
    sizes = models.CharField(max_length=50)
    production_date = models.DateField(auto_now_add=True)
    produced_items = models.IntegerField(blank=True, null=True)

class Sewing(models.Model):
    cutting = models.ForeignKey(Cutting, on_delete=models.CASCADE)
    sewing_date = models.DateField()
    items_produced = models.IntegerField()
    size = models.CharField(max_length=50)

class Ironing(models.Model):
    cutting = models.ForeignKey(Cutting, on_delete=models.CASCADE)
    ironing_date = models.DateField()
    items_ironed = models.IntegerField()

class Contact(models.Model):
    PERSON_CHOICES = [
        ('C', 'Cutter'),
        ('S', 'Sewer'),
        ('I', 'Ironer'),
    ]
    person_type = models.CharField(max_length=1, choices=PERSON_CHOICES)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100, blank=True, null=True)
    machine_number = models.IntegerField(blank=True, null=True)
