# Generated by Django 4.2.3 on 2023-08-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_userprofile_certification_files_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificationfile',
            name='certification',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='certification_files',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='highest_education',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='job_applying_for',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='previously_employed_job',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education_course_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='most_recent_job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='certifications',
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='CertificationFile',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='PreviousJob',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='certifications',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
