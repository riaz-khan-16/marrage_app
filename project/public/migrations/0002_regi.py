# Generated by Django 4.2.3 on 2023-08-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=100)),
                ('password', models.IntegerField(max_length=100)),
            ],
        ),
    ]