# Generated by Django 5.0.7 on 2024-08-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
