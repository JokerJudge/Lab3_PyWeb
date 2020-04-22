# Generated by Django 3.0.4 on 2020-04-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(null=True)),
                ('price_sale', models.PositiveIntegerField()),
                ('image', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
    ]
