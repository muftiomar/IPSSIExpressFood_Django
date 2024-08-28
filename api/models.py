from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Courier(models.Model):
    STATUS_CHOICES = (
        ('free', 'Free'),
        ('delivering', 'Delivering')
    )

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='free')
    location = models.JSONField()

    def __str__(self):
        return self.name

class Order(models.Model):
    DELIVERY_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('delivered', 'Delivered')
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='pending')
    courier = models.ForeignKey(Courier, null=True, blank=True, on_delete=models.SET_NULL)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
