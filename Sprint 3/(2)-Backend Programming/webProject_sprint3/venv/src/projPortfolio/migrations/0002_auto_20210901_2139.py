# Generated by Django 3.2.6 on 2021-09-01 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio_artproj',
            name='description',
        ),
        migrations.RemoveField(
            model_name='portfolio_artproj',
            name='image',
        ),
        migrations.RemoveField(
            model_name='portfolio_softproj',
            name='image',
        ),
    ]
