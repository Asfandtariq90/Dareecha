# Generated by Django 4.2 on 2023-04-27 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('companion_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'companion',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('model_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('vendor', models.CharField(max_length=20)),
                ('model', models.CharField(default='Unknown', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CompanionUser',
            fields=[
                ('appuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='baham.appuser')),
            ],
            bases=('baham.appuser',),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('appuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='baham.appuser')),
            ],
            bases=('baham.appuser',),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('contract_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('companion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baham.companion')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.vehicle')),
            ],
        ),
    ]
