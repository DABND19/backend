# Generated by Django 3.1.4 on 2021-01-26 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='legaladdress',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.organisation'),
            preserve_default=False,
        ),
    ]