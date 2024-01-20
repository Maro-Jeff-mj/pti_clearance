# Generated by Django 4.2.3 on 2023-09-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_staffprofile_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Null', 'Null')], max_length=6)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
