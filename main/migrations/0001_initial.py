# Generated by Django 2.2.5 on 2019-09-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Your_pic', models.ImageField(upload_to='images/')),
                ('Your_details', models.TextField()),
            ],
        ),
    ]
