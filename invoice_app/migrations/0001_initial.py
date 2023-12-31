# Generated by Django 4.1.7 on 2023-03-21 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('invoice_no', models.CharField(max_length=50)),
                ('customername', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('nvoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_details', to='invoice_app.invoice')),
            ],
        ),
    ]
