# Generated by Django 3.2.2 on 2021-05-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_consultation_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('useremail', models.EmailField(max_length=100)),
                ('doctoremail', models.EmailField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Consultation',
        ),
    ]
