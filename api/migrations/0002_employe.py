# Generated by Django 3.1.8 on 2024-05-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('employe_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
    ]
