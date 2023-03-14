# Generated by Django 4.1 on 2023-03-12 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_women_delete_followrs_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='templatetags',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='university.category'),
            preserve_default=False,
        ),
    ]