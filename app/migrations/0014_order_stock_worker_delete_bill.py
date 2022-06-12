# Generated by Django 4.0.4 on 2022-06-12 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_bill_bill_num_bill_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cretated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Delivered', 'Delivered'), ('Not-Delivered', 'not-Delivered')], max_length=20, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('quantity', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('place', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
    ]