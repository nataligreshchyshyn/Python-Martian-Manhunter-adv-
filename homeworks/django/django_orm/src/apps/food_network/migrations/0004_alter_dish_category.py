# Generated by Django 3.2.6 on 2021-08-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_network', '0003_auto_20210805_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ManyToManyField(related_name='dishes', to='food_network.Menu'),
        ),
    ]
