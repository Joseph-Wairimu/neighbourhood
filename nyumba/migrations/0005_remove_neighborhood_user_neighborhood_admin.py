# Generated by Django 4.0.4 on 2022-04-18 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nyumba', '0004_rename_admin_neighborhood_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='user',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='nyumba.profile'),
        ),
    ]