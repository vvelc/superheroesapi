# Generated by Django 3.2.4 on 2021-06-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh_app', '0006_alter_superhero_hero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='hero_image',
            field=models.ImageField(default='http://via.placeholder.com/300', upload_to='assets/hero_images'),
        ),
    ]
