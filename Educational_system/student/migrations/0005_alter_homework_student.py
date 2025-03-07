# Generated by Django 5.0.6 on 2024-06-29 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_homework'),
        ('system', '0006_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='system.student'),
        ),
    ]
