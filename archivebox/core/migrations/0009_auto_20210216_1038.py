# Generated by Django 3.1.3 on 2021-02-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210105_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshot',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, null=True),
        ),
    ]