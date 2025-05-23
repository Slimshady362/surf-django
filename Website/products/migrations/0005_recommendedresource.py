# Generated by Django 4.2.5 on 2024-04-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_resource_resource_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=100)),
                ('resource_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]
