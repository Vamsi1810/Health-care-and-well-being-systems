# Generated by Django 3.2.2 on 2021-05-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('hospital', models.CharField(max_length=100)),
                ('problem', models.CharField(choices=[('Allergies', 'Allergies'), ('Cold and Flu', 'Cold and Flu'), ('Conjunctivitis (pink eye)', 'Conjunctivitis (pink eye)'), ('Diarrhea', 'Diarrhea'), ('Headache', 'Headache'), ('Mononucleosis', 'Mononucleosis'), ('Stomach Ache', 'Stomach Ache'), ('Nausea and Vomiting', 'Nausea and Vomiting')], default='Allergies', max_length=100)),
                ('date', models.DateField()),
                ('slot', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon')], default='morning', max_length=50)),
                ('confirmation', models.CharField(choices=[('email', 'email'), ('phone number', 'phone number')], default='email', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(choices=[('Anantapur', 'Anantapur'), ('Chittoor', 'Chittoor'), ('East Godavari', 'East Godavari'), ('Guntur', 'Guntur'), ('Kadapa', 'Kadapa'), ('Krishna', 'Krishna'), ('Kurnool', 'Kurnool'), ('Nellore', 'Nellore'), ('Prakasam', 'Prakasam'), ('Srikakulam', 'Srikakulam'), ('Vishakapatnam', 'Vishakapatnam'), ('Viziayanagaram', 'Viziayanagaram'), ('West Godavari', 'West Godavari')], default='Anantapur', max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('agreement', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('mobile', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(choices=[('Anantapur', 'Anantapur'), ('Chittoor', 'Chittoor'), ('East Godavari', 'East Godavari'), ('Guntur', 'Guntur'), ('Kadapa', 'Kadapa'), ('Krishna', 'Krishna'), ('Kurnool', 'Kurnool'), ('Nellore', 'Nellore'), ('Prakasam', 'Prakasam'), ('Srikakulam', 'Srikakulam'), ('Vishakapatnam', 'Vishakapatnam'), ('Viziayanagaram', 'Viziayanagaram'), ('West Godavari', 'West Godavari')], default='Anantapur', max_length=50)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]
