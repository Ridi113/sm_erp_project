# Generated by Django 3.0.5 on 2020-04-12 04:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sm_hr', '0008_auto_20200412_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]