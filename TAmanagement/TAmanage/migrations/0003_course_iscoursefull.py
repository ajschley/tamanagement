# Generated by Django 2.2.6 on 2019-10-31 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAmanage', '0002_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isCourseFull',
            field=models.BooleanField(default=False),
        ),
    ]