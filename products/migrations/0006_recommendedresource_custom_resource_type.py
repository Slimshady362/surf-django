# Generated by Django 4.2.5 on 2024-04-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_recommendedresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedresource',
            name='custom_resource_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
