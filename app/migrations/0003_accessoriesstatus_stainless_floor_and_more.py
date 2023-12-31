# Generated by Django 4.2.2 on 2023-07-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_accessory_description_accessorytranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessoriesstatus',
            name='stainless_floor',
            field=models.BooleanField(default=False, verbose_name='Stainless Floor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessoriesstatus',
            name='stall',
            field=models.BooleanField(default=False, verbose_name='Stall'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accessoriesstatus',
            name='metal_plate',
            field=models.BooleanField(verbose_name='Side Protection Bar'),
        ),
        migrations.AlterField(
            model_name='accessoriesstatus',
            name='more_cylinder',
            field=models.BooleanField(verbose_name='Addition Cylinder'),
        ),
        migrations.AlterField(
            model_name='accessoriesstatus',
            name='three_fold_gate',
            field=models.BooleanField(verbose_name='3 Fold Gate'),
        ),
        migrations.AlterField(
            model_name='accessoriesstatus',
            name='two_fold_gate',
            field=models.BooleanField(verbose_name='2 Fold Gate'),
        ),
    ]
