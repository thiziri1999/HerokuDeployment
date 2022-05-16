from django.db import models
class Project(models.Model):
    title=models.CharField(max_length=100)
    technologie=models.CharField(max_length=100)

    description=models.CharField(max_length=300)
    image=models.ImageField( upload_to='PortfoliosAPP/images/')
    url=models.FileField(upload_to='PortfoliosAPP/images/')
    def __str__(self):
        return self.title

    