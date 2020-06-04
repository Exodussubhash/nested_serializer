# Generated by Django 3.0.5 on 2020-06-04 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True)),
                ('activity_periods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='api_app.User')),
            ],
        ),
    ]
