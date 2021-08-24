# Generated by Django 3.2.4 on 2021-07-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='color',
            field=models.TextField(max_length=80, null=True, verbose_name='Color del producto'),
        ),
        migrations.AddField(
            model_name='ventas',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='Precio del producto'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='cantidad',
            field=models.TextField(max_length=10, null=True, verbose_name='Cantidad en stock'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='descripcion',
            field=models.CharField(max_length=500, null=True, verbose_name='Descripcion del producto'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía del producto'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='nombre',
            field=models.TextField(max_length=80, null=True, verbose_name='Nombre del producto'),
        ),
    ]