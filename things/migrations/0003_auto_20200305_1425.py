# Generated by Django 3.0.4 on 2020-03-05 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_auto_20190501_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='things.Country'),
        ),
    ]
