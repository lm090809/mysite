# Generated by Django 2.1.4 on 2019-03-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorgwardEngineDiagnostics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_description', models.TextField(blank=True, null=True)),
                ('parts', models.CharField(blank=True, max_length=255, null=True)),
                ('performance', models.TextField(blank=True, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('solution', models.TextField(blank=True, null=True)),
                ('vehicle_system', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'borgward_engine_diagnostics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tboxdata',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='key', primary_key=True, serialize=False)),
                ('tbox_data', models.TextField(blank=True, db_column='TBOX_data', null=True)),
                ('vin', models.TextField(blank=True, db_column='VIN', null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('sid', models.TextField(blank=True, db_column='SID', null=True)),
                ('detail', models.TextField(blank=True, db_column='detail', null=True)),
            ],
            options={
                'db_table': 'tbox_data',
                'managed': False,
            },
        ),
    ]
