# Generated by Django 3.2.8 on 2023-05-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_rename_cpga_applicant_cgpa_application_predicted_aid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='propertystatus',
            field=models.CharField(max_length=25),
        ),
    ]