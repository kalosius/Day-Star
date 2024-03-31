# Generated by Django 5.0.3 on 2024-03-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycare', '0002_alter_baby_options_alter_procurement_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitter',
            name='contacts',
        ),
        migrations.AddField(
            model_name='sitter',
            name='contact1',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='sitter',
            name='contact2',
            field=models.CharField(max_length=16, null=True),
        ),
    ]