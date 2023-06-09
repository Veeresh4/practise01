# Generated by Django 4.2 on 2023-05-04 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_country_brand_remove_country_person_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='person_name',
        ),
        migrations.AddField(
            model_name='person',
            name='country_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='app.country'),
        ),
        migrations.AddField(
            model_name='pet',
            name='person_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='app.person'),
        ),
    ]
