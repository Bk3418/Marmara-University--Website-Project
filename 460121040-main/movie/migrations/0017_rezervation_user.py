# Generated by Django 4.0 on 2023-01-03 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movie', '0016_rezervation'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]