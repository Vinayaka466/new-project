# Generated by Django 5.1.3 on 2024-11-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0003_cart_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('complaint', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creadted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='User',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='Products',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='User',
            new_name='user',
        ),
    ]