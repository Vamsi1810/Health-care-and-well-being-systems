# Generated by Django 3.2.2 on 2021-05-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20210513_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.EmailField(max_length=100)),
                ('doctoremail', models.EmailField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
