# Generated by Django 3.1.1 on 2021-06-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='photos/covers/%Y/%m/%d/'),
        ),
    ]
