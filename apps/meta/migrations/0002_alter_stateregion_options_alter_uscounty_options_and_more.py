# Generated by Django 4.0 on 2022-10-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stateregion',
            options={'ordering': ['-country', 'name'], 'verbose_name': 'State/Region/Province', 'verbose_name_plural': 'States/Regions/Provinces'},
        ),
        migrations.AlterModelOptions(
            name='uscounty',
            options={'ordering': ['name'], 'verbose_name_plural': 'US Counties'},
        ),
        migrations.AlterField(
            model_name='stateregion',
            name='location_class',
            field=models.CharField(choices=[('us-state', 'US State'), ('us-region', 'US Region'), ('us-other', 'US Other'), ('ca-province', 'Canada Province'), ('canada', 'Canada'), ('us-county', 'County')], max_length=40, verbose_name='Location Class'),
        ),
        migrations.AlterField(
            model_name='uscounty',
            name='location_class',
            field=models.CharField(choices=[('us-state', 'US State'), ('us-region', 'US Region'), ('us-other', 'US Other'), ('ca-province', 'Canada Province'), ('canada', 'Canada'), ('us-county', 'County')], max_length=40, verbose_name='Location Class'),
        ),
    ]
