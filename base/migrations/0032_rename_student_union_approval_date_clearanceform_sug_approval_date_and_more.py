# Generated by Django 4.2.3 on 2023-09-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_rename_student_affair_approval_date_clearanceform_chief_liberian_approval_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clearanceform',
            old_name='student_union_approval_date',
            new_name='sug_approval_date',
        ),
        migrations.RenameField(
            model_name='clearanceform',
            old_name='student_union_comment',
            new_name='sug_comment',
        ),
        migrations.RenameField(
            model_name='clearanceform',
            old_name='student_union_review',
            new_name='sug_review',
        ),
        migrations.AlterField(
            model_name='clearanceform',
            name='boys_hostel_review',
            field=models.CharField(default='null', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='clearanceform',
            name='department',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Industrial Safety and Environmental', 'Industrial Safety and Environmental'), ('Mineral and Petroleum Resources', 'Mineral and Petroleum Resources'), ('Petroleum and Natural Gas', 'Petroleum and Natural Gas'), ('Petroleum Engineering and Geoscience', 'Petroleum Engineering and Geoscience'), ('Petroleum Marketing and Business Studies', 'Petroleum Marketing and Business Studies'), ('Science Laboratory Technology', 'Science Laboratory Technology'), ('Welding and Fabrication', 'Welding and Fabrication'), ('Computer Engineering', 'Computer Engineering'), ('Mechatronics', 'Mechatronics')], max_length=50),
        ),
        migrations.AlterField(
            model_name='clearanceform',
            name='nddc_hostel_review',
            field=models.CharField(default='null', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='clearanceform',
            name='noble_hostel_review',
            field=models.CharField(default='null', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='clearanceform',
            name='ptdf_wing_a_review',
            field=models.CharField(default='null', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='clearanceform',
            name='ptdf_wing_b_review',
            field=models.CharField(default='null', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='department',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Industrial Safety and Environmental', 'Industrial Safety and Environmental'), ('Mineral and Petroleum Resources', 'Mineral and Petroleum Resources'), ('Petroleum and Natural Gas', 'Petroleum and Natural Gas'), ('Petroleum Engineering and Geoscience', 'Petroleum Engineering and Geoscience'), ('Petroleum Marketing and Business Studies', 'Petroleum Marketing and Business Studies'), ('Science Laboratory Technology', 'Science Laboratory Technology'), ('Welding and Fabrication', 'Welding and Fabrication'), ('Computer Engineering', 'Computer Engineering'), ('Mechatronics', 'Mechatronics')], max_length=50),
        ),
    ]