# Generated by Django 3.2.1 on 2022-02-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('0', 'PENDING'), ('1', 'COMPLETED')], max_length=2),
        ),
    ]
