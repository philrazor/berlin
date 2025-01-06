from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make.name} {self.name}"

class Part(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="parts")
    name = models.CharField(max_length=100 , blank=True , null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True ,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    year = models.PositiveIntegerField(blank=True , null=True)
    engine_code = models.CharField(max_length=50, blank=True, null=True)
    engine_capacity = models.PositiveIntegerField(help_text="Engine capacity in cc", blank=True, null=True)
    condition = models.CharField(max_length=250 ,blank=True , null=True)

    def __str__(self):
        return f"{self.name} for {self.car_model} - {self.price} dirhams"


class PartImage(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='part_images/')

    def __str__(self):
        return f"Image for {self.part.name}"
