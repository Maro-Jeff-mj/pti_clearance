# Generated by Django 4.2.3 on 2023-09-06 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_dummyform_student_affair_reviev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dummyform',
            old_name='student_affair_reviev',
            new_name='student_affair_review',
        ),
    ]
