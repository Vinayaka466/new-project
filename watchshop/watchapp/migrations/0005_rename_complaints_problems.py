# Generated by Django 5.1.3 on 2024-11-24 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0004_complaints_rename_user_cart_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complaints',
            new_name='Problems',
        ),
    ]
