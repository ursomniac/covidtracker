# Generated by Django 4.0 on 2022-10-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StateRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Location')),
                ('abbreviation', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abbreviation')),
                ('population', models.PositiveIntegerField(blank=True, null=True, verbose_name='Population')),
                ('country', models.CharField(choices=[('US', 'USA'), ('CA', 'Canada')], max_length=2, verbose_name='Country')),
                ('location_class', models.CharField(choices=[('us-state', 'US State'), ('us-region', 'US Region'), ('us-other', 'US Other'), ('ca-province', 'Canada Province'), ('canada', 'Canada')], max_length=40, verbose_name='Location Class')),
                ('swing_2016', models.FloatField(blank=True, null=True, verbose_name='Swing 2016')),
                ('swing_2020', models.FloatField(blank=True, null=True, verbose_name='Swing 2020')),
                ('swing_2022', models.FloatField(blank=True, null=True, verbose_name='Swing 2022')),
            ],
            options={
                'ordering': ['-country', 'name'],
            },
        ),
        migrations.CreateModel(
            name='USCounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Location')),
                ('abbreviation', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abbreviation')),
                ('population', models.PositiveIntegerField(blank=True, null=True, verbose_name='Population')),
                ('country', models.CharField(choices=[('US', 'USA'), ('CA', 'Canada')], max_length=2, verbose_name='Country')),
                ('location_class', models.CharField(choices=[('us-state', 'US State'), ('us-region', 'US Region'), ('us-other', 'US Other'), ('ca-province', 'Canada Province'), ('canada', 'Canada')], max_length=40, verbose_name='Location Class')),
                ('swing_2016', models.FloatField(blank=True, null=True, verbose_name='Swing 2016')),
                ('swing_2020', models.FloatField(blank=True, null=True, verbose_name='Swing 2020')),
                ('swing_2022', models.FloatField(blank=True, null=True, verbose_name='Swing 2022')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
