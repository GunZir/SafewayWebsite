# Generated by Django 4.2.2 on 2023-07-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_accessoriesstatus_stainless_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='image_src',
            field=models.ImageField(blank=True, null=True, upload_to='images/accessory'),
        ),
        migrations.AlterField(
            model_name='dumphoist',
            name='image_src',
            field=models.ImageField(blank=True, null=True, upload_to='images/dumphoist/'),
        ),
    ]
