# Generated by Django 3.1.6 on 2021-02-14 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=700, upload_to='', verbose_name='image', width_field=525)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(max_length=500, verbose_name='description')),
                ('color', models.CharField(max_length=6, null=True, verbose_name='color')),
                ('isChild', models.BooleanField(verbose_name='is child')),
                ('size', models.DecimalField(decimal_places=2, max_digits=70, verbose_name='size')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100000, verbose_name='price')),
                ('moderated', models.BooleanField(default=False, verbose_name='moderated')),
                ('_type', models.CharField(choices=[('JACKET', 'Jacket'), ('COAT', 'Coat'), ('HOODY', 'Hoody'), ('T_SHIRT', 'T-shirt'), ('SHIRT', 'Shirt'), ('PANTS', 'Pants'), ('DENIM', 'Denim'), ('SNEAKERS', 'Sneakers'), ('BOOTS', 'Boots'), ('UNDERWEAR', 'Underwear'), ('ACCESSORIES', 'Accessories'), ('DEFAULT', 'Other')], default='DEFAULT', max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
