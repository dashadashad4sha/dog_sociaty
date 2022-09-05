# Generated by Django 4.0.1 on 2022-01-24 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_doggy_category_alter_doggy_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doggy',
            name='category',
        ),
        migrations.AddField(
            model_name='doggy',
            name='category_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
    ]
