# Generated by Django 4.1.7 on 2023-03-21 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='nvoice',
            new_name='invoice',
        ),
    ]
