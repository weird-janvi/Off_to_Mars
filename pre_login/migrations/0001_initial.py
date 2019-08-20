# Generated by Django 2.2.4 on 2019-08-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Details',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('Age', models.IntegerField(default=19)),
                ('City', models.CharField(default='Bangalore', max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(default='India', max_length=30)),
                ('Occupation', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
