# Generated by Django 3.1.5 on 2021-03-18 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210317_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'Product Image', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
