# Generated by Django 5.0 on 2024-01-05 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='publicationlink',
            unique_together={('reviewer', 'article')},
        ),
    ]
