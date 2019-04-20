# Generated by Django 2.1.7 on 2019-04-15 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('big_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.LocalCategory')),
            ],
            options={
                'verbose_name': 'type',
                'verbose_name_plural': 'types',
                'ordering': ['name'],
            },
        ),
    ]
