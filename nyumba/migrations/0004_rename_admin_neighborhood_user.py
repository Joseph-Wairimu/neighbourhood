# Generated by Django 4.0.4 on 2022-04-18 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyumba', '0003_alter_neighborhood_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='admin',
            new_name='user',
        ),
    ]
