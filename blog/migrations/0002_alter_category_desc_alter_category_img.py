# Generated by Django 5.0.3 on 2024-04-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]
