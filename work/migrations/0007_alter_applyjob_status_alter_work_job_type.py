# Generated by Django 5.1 on 2024-08-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_alter_work_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Pending', 'Pending')], max_length=20),
        ),
        migrations.AlterField(
            model_name='work',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Hybrid', 'Hybrid'), ('Remote', 'Remote'), ('Onsite', 'Onsite')], max_length=50, null=True),
        ),
    ]
