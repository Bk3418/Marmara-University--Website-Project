# Generated by Django 4.0 on 2023-01-02 18:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movie', '0008_remove_about_ototamir_id_remove_adres_musteri_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('Contact_us_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Message', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('Home_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=250)),
                ('aciklama', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('Img', models.ImageField(upload_to='movie/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('Musteri_ID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OtoTamir',
            fields=[
                ('OtoTamir_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Adres', models.CharField(max_length=250)),
                ('Number', models.CharField(max_length=25)),
                ('Mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Servis',
            fields=[
                ('Servis_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('Testimonial_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Yorum', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('Musteri_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.musteri')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('Person_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Full_name', models.CharField(max_length=250)),
                ('Img', models.ImageField(upload_to='movie/images/')),
                ('Brithday', models.DateField()),
                ('Kayıt_date', models.DateField(auto_now=True)),
                ('Number', models.CharField(max_length=250)),
                ('Mail', models.EmailField(max_length=254)),
                ('Servis_ID', models.ManyToManyField(to='movie.Servis')),
            ],
        ),
        migrations.CreateModel(
            name='Furnitures',
            fields=[
                ('Furnitures_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Aciklama', models.CharField(max_length=250)),
                ('Img', models.ImageField(upload_to='movie/images/')),
                ('Servis_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.servis')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('Car_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Marka', models.CharField(max_length=250)),
                ('Model', models.CharField(max_length=250)),
                ('Yil', models.CharField(max_length=250)),
                ('Musteri_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.musteri')),
                ('Servis_ID', models.ManyToManyField(to='movie.Servis')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('Adres_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('il', models.CharField(max_length=50)),
                ('ilce', models.CharField(max_length=50)),
                ('mahalle_no', models.IntegerField()),
                ('Musteri_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.musteri')),
                ('Person_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.person')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('About_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=250)),
                ('altbaslik', models.CharField(max_length=250)),
                ('aciklama', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('OtoTamir_ID', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.ototamir')),
            ],
        ),
    ]