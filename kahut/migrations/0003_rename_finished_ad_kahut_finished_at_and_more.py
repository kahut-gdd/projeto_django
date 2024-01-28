# Generated by Django 5.0.1 on 2024-01-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kahut", "0002_alter_kahut_deadline_alter_kahut_finished_ad"),
    ]

    operations = [
        migrations.RenameField(
            model_name="kahut",
            old_name="finished_ad",
            new_name="finished_at",
        ),
        migrations.AlterField(
            model_name="kahut",
            name="deadline",
            field=models.DateField(verbose_name="data de entrega"),
        ),
        migrations.AlterField(
            model_name="kahut",
            name="tittle",
            field=models.CharField(max_length=100, verbose_name="Título"),
        ),
    ]