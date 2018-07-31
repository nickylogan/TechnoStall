# Generated by Django 2.0.7 on 2018-07-31 18:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tsmanager', '0006_auto_20180801_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_edited', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tsmanager.Item')),
            ],
        ),
        migrations.RenameField(
            model_name='restock',
            old_name='PIC',
            new_name='restock_PIC',
        ),
    ]
