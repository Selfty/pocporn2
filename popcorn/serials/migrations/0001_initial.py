# Generated by Django 3.1.5 on 2021-01-16 11:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=200)),
                ('title_cz', models.CharField(max_length=200)),
                ('title_sk', models.CharField(max_length=200)),
                ('popis', models.TextField(default='')),
                ('url1', models.CharField(max_length=400)),
                ('url2', models.CharField(max_length=400)),
                ('image', models.CharField(max_length=200)),
                ('start_yr', models.IntegerField(default=0)),
                ('end_yr', models.IntegerField(default=0)),
                ('delka', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Zaner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Topserials',
            fields=[
                ('serial', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='serials.serial')),
                ('image', models.CharField(default='brickleberry_small.jpg', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='serial',
            name='zaner',
            field=models.ManyToManyField(to='serials.Zaner'),
        ),
        migrations.CreateModel(
            name='Epizoda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulek_cz', models.CharField(max_length=200)),
                ('titulek_en', models.CharField(max_length=200)),
                ('titulek_sk', models.CharField(max_length=200)),
                ('cislo_serie', models.IntegerField()),
                ('cislo_epizoda', models.IntegerField()),
                ('popis_epizody', models.TextField()),
                ('url1', models.TextField(default='')),
                ('url1_cc', models.IntegerField(default=0)),
                ('url2', models.TextField(default='')),
                ('url2_cc', models.IntegerField(default=0)),
                ('url3', models.TextField(default='')),
                ('url3_cc', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('epizoda_serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serials.serial')),
            ],
        ),
    ]
