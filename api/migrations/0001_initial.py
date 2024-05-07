# Generated by Django 3.1.8 on 2024-05-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
                ('types', models.CharField(choices=[('ID', 'ID'), ('non it', 'not it'), ('mobile', 'phone')], max_length=100)),
            ],
        ),
    ]