# Generated by Django 3.2.4 on 2021-07-08 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=80, verbose_name='Descripcion del producto')),
                ('nombre', models.TextField(verbose_name='Nombre del producto')),
                ('cantidad', models.TextField(verbose_name='Cantidad en stock')),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía del curso')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['-created'],
            },
        ),
    ]
