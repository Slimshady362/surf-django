# Generated by Django 4.2.5 on 2023-10-02 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_videoresource_websiteresource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('resource_type', models.CharField(choices=[('video', 'Video'), ('website', 'Website')], default='website', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='VideoResource',
        ),
        migrations.DeleteModel(
            name='WebsiteResource',
        ),
        migrations.AddField(
            model_name='resource',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.topic'),
        ),
    ]
