# Generated by Django 2.2.7 on 2019-11-10 18:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TAmanage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userEmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userPassword',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_type',
            new_name='userType',
        ),
        migrations.RemoveField(
            model_name='course',
            name='isCourseFull',
        ),
        migrations.AddField(
            model_name='course',
            name='graderTAs',
            field=models.ManyToManyField(blank=True, related_name='courses', to='TAmanage.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TAmanage.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='firstName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='officeHours',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='officeHoursDates',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='officeLocation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='endTime',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='End Time:'),
        ),
        migrations.AlterField(
            model_name='course',
            name='startTime',
            field=models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Start Time:'),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('startTime', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Start Time:')),
                ('endTime', models.TimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='End Time:')),
                ('dates', models.CharField(default='MTWRFS', max_length=6)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TAmanage.Course')),
                ('ta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TAmanage.User')),
            ],
        ),
    ]
