# Generated by Django 2.1.7 on 2019-04-15 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='big_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
    ]
