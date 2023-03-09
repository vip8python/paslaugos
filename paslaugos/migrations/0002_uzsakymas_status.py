# Generated by Django 4.1.7 on 2023-03-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paslaugos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzsakymas',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Priimtas'), ('v', 'Vykdomas'), ('i', 'Įvykdytas'), ('a', 'Apmokėtas')], default='s', help_text='Pažymėti užsakymo statusą, pirminis - "Suformuotas"', max_length=1, verbose_name='Užsakymo statusas'),
        ),
    ]
