# Generated by Django 5.0 on 2023-12-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_remove_employee_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_birth',
            field=models.DateField(default='1990-01-01'),
        ),
    ]
