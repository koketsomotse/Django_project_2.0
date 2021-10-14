from django.db import models

# Create your models here.


class Task(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    taskname = models.CharField(max_length=200)
    taskdescription = models.CharField(max_length=200)
    taskfeatures = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.taskname


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
    fristname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    cellnumber = models.IntegerField()
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
