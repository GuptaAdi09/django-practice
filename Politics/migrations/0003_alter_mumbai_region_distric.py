# Generated by Django 5.1.5 on 2025-01-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Politics', '0002_mumbai_region_distric_alter_candidate_candidate_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mumbai_region',
            name='distric',
            field=models.CharField(default='Mumbai', max_length=100),
        ),
    ]
