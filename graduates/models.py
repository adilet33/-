from django.db import models



class Department(models.Model):
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=100)

    
    def __str__(self) -> str:
        return self.name





class Graduate(models.Model):
    EMPLOYMENT_STATUS = (('employed', 'Employed'), ('unemployed','Unemployed'))

    name = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='No job')
    graduation_year = models.PositiveIntegerField()
    employment_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS, default='unemployed')


    def __str__(self) -> str:
        return self.name