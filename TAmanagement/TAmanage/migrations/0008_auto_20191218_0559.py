# Generated by Django 2.2.6 on 2019-12-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAmanage', '0007_remove_course_iscoursefull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='location',
            field=models.CharField(blank=True, default='Online', max_length=255, null=True),
        ),
    ]
