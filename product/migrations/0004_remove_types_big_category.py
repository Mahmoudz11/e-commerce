# Generated by Django 2.1.7 on 2019-04-15 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190415_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='types',
            name='big_category',
        ),
    ]