# Generated by Django 2.2.6 on 2019-10-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(default='CS361', max_length=29)),
                ('isFull', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.CharField(max_length=50)),
                ('userPassword', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('ADMIN', 'Admin'), ('PROF', 'Professor'), ('TA', 'TA / Grader')], default='TA', max_length=5)),
            ],
        ),
    ]
