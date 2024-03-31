from django.db import models

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    next_of_kin = models.CharField(max_length=100)
    nin = models.CharField(max_length=14)
    recommender_name = models.CharField(max_length=100)
    religion = models.CharField(max_length=50, null=True, blank=True)
    education_level = models.CharField(max_length=50)
    sitter_number = models.IntegerField(unique=True)
    contacts = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Baby(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    brought_by = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(auto_now_add=True)
    parents_names = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    period_of_stay = models.CharField(max_length=100)
    baby_number = models.IntegerField(unique=True)
    checked_out = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Babies"


class Payment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20)  # Half day or Full day
    timestamp = models.DateTimeField(auto_now_add=True)


class Procurement(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Procurement"
