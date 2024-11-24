# Generated by Django 5.1.3 on 2024-11-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0005_rename_complaints_problems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('complaint', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creadted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Problems',
            new_name='Complaints',
        ),
    ]
