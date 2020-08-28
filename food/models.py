from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name
     
class Product(models.Model):
    sizes = (('S', 'Small'),('M', 'Medium'), ('L', 'Large'))
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food/', blank=True)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=sizes, default='M')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    


