# Generated by Django 2.2.16 on 2020-10-27 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0010_add_staging_rejected_repos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionimport',
            name='task_id',
            field=models.OneToOneField(db_column='task_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='galaxy_import', serialize=False, to='ansible.CollectionImport'),
        ),
    ]
