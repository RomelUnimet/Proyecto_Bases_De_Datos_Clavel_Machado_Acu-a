from django.db import models

# Create your models here.




class Job(models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Genero(models.Model):
    sexo=models.CharField(max_length=30)

    def __str__(self):
        return self.sexo

class Employee(models.Model):
    ci=models.CharField(max_length=60)
    name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    phone= models.CharField(max_length=20)
    points= models.IntegerField()
    adress=models.CharField(max_length=200)
    gender= models.ForeignKey(Genero, on_delete=models.CASCADE, default="Hombre")
    birth_date=models.DateField()
    job_id=models.ForeignKey(Job, on_delete=models.CASCADE)
    is_active=models.BooleanField()

    def __str__(self):
        return self.last_name




