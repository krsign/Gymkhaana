# Generated by Django 2.2 on 2020-08-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=1),
        ),
    ]
