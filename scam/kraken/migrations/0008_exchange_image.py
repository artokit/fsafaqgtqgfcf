# Generated by Django 4.1.6 on 2023-03-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kraken', '0007_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='image',
            field=models.ImageField(default='default_avatar2.jpeg', upload_to=''),
        ),
    ]
