# Generated by Django 2.2 on 2021-01-23 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200910_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_people', to='accounts.Profile', verbose_name='от_человека')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_people', to='accounts.Profile', verbose_name='к_человеку')),
            ],
            options={
                'verbose_name': 'Друг/Подруга',
                'verbose_name_plural': 'Друзья/Подруги',
            },
        ),
    ]
