# Generated by Django 4.1.4 on 2022-12-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=255)),
                ('driver_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='ambulances')),
            ],
        ),
        migrations.CreateModel(
            name='CreateQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.CharField(choices=[('CARDIOLOGY', 'CARDIOLOGY'), ('NEUROLOGY', 'NEUROLOGY'), ('ORTHOPEDICS', 'ORTHOPEDICS'), ('CANCER DEPARTMENT', 'CANCER DEPARTMENT'), ('OPHTHALMOLOGY', 'OPHTHALMOLOGY'), ('RESPIRATORY', 'RESPIRATORY')], max_length=21)),
                ('describe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Get_touch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]
