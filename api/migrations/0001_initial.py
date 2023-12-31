# Generated by Django 4.2.3 on 2023-07-19 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_code', models.CharField(max_length=20, unique=True)),
                ('lval30', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='IndexHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('low', models.DecimalField(blank=True, decimal_places=1, max_digits=8)),
                ('high', models.DecimalField(blank=True, decimal_places=1, max_digits=8)),
                ('close', models.DecimalField(blank=True, decimal_places=1, max_digits=8)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='api.index')),
            ],
        ),
    ]
