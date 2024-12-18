# Generated by Django 5.1.3 on 2024-11-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchapp', '0008_delete_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
