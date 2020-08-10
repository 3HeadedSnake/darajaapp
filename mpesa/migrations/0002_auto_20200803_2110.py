# Generated by Django 3.0.8 on 2020-08-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='C2BPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Balance',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='CheckoutRequestID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='MerchantRequestID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='MpesaReceiptNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='PhoneNumber',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='ResultCode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='ResultDesc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='TransactionDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]