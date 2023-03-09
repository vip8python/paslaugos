# Generated by Django 4.1.7 on 2023-03-09 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobilioModelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marke', models.CharField(max_length=50)),
                ('modelis', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Automobilio modelis',
                'verbose_name_plural': 'Automobilio modeliai',
                'db_table': 'automobilio modelis',
            },
        ),
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valstybinis_nr', models.CharField(max_length=20)),
                ('vin_kodas', models.CharField(max_length=20, null=True)),
                ('klientas', models.CharField(max_length=50, null=True)),
                ('automobilio_modelis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paslaugos.automobiliomodelis')),
            ],
            options={
                'verbose_name': 'Automobilis',
                'verbose_name_plural': 'Automobiliai',
                'db_table': 'automobilis',
            },
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(max_length=50, null=True)),
                ('kaina', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
            options={
                'verbose_name': 'Paslauga',
                'verbose_name_plural': 'Paslaugos',
                'db_table': 'paslaugos',
            },
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('suma', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('automobilis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paslaugos.automobilis')),
            ],
            options={
                'verbose_name': 'Uzsakymas',
                'verbose_name_plural': 'Uzsakymai',
                'db_table': 'uzsakymas',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='UzsakymoEilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiekis', models.IntegerField(default=0)),
                ('kaina', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('paslauga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paslaugos.paslauga')),
                ('uzsakymas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paslaugos.uzsakymas')),
            ],
            options={
                'verbose_name': 'Uzsakymo eilute',
                'verbose_name_plural': 'Uzsakymo eilutes',
                'db_table': 'uzsakymo eilutes',
            },
        ),
    ]
