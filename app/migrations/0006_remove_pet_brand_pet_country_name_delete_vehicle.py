# Generated by Django 4.2 on 2023-05-05 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_person_brand_remove_person_country_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='brand',
        ),
        migrations.AddField(
            model_name='pet',
            name='country_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='app.country'),
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
