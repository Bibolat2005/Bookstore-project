# Generated by Django 5.0.3 on 2024-04-21 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_book_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Cart',
            },
        ),
    ]
