# Generated by Django 4.2.5 on 2023-09-11 20:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rol_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('type_document', models.CharField(max_length=20)),
                ('document', models.PositiveSmallIntegerField()),
                ('birthday', models.DateField()),
                ('phone_number', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=60)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='crud.roles')),
            ],
        ),
    ]
