# Generated by Django 3.2.20 on 2023-08-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='modified_data',
        ),
        migrations.AddField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]