# Generated by Django 4.2 on 2023-05-04 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True)),
                ('profession', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('citizenship', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('varient', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='app.vehicle')),
                ('person_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='app.person')),
                ('pet_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='app.pet')),
            ],
        ),
    ]
