# Generated by Django 3.1.6 on 2021-02-24 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ticket_choice', models.CharField(choices=[('Bug', 'Bug'), ('Enhancement', 'Enhancement'), ('New_Feature', 'New Feature')], default='Bug', max_length=20)),
                ('issue_description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('ticket_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=75)),
                ('comment_text', models.CharField(max_length=550)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='issue_tracker.ticket')),
            ],
        ),
        migrations.CreateModel(
            name='AdminTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_choice', models.CharField(blank=True, choices=[('Critical', 'Critical'), ('High', 'High'), ('Normal', 'Normal')], max_length=10, null=True)),
                ('status_choice', models.CharField(blank=True, choices=[('Open', 'Open'), ('Pending', 'Pending'), ('Closed', 'Closed')], max_length=10, null=True)),
                ('additional_comments', models.CharField(blank=True, max_length=350, null=True)),
                ('admin_ticket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='issue_tracker.ticket')),
            ],
        ),
    ]
