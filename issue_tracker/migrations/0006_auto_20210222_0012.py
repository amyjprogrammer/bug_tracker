# Generated by Django 3.1.6 on 2021-02-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0005_auto_20210221_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminticket',
            name='priority_choice',
            field=models.CharField(blank=True, choices=[('Critical', 'Critical'), ('High', 'High'), ('Normal', 'Normal')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='adminticket',
            name='status_choice',
            field=models.CharField(blank=True, choices=[('Open', 'Open'), ('Pending', 'Pending'), ('Closed', 'Closed')], max_length=10, null=True),
        ),
    ]