from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    species = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=250, null=True, blank=True)
    availability = models.BooleanField(default=True)
    adopted_time = models.DateTimeField(auto_now_add=True)
    siblings = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.name} - {self.species}"

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ["name"]


class Owner(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    optional_message = models.TextField(blank=True, null=True)
    request_time = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Pet,blank=True,
        null=True,on_delete=models.CASCADE)
    sub_owner = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"
        ordering = ["first_name"]
