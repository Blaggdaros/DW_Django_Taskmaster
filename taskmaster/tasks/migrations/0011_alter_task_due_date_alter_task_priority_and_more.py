# Generated by Django 4.2.1 on 2023-05-19 17:06

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True, validators=[tasks.models.date_in_future], verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Prioridad baja'), ('N', 'Prioridad normal'), ('H', 'Prioridad alta')], default='N', max_length=1, verbose_name='Prioridad'),
        ),
        migrations.AlterField(
            model_name='task',
            name='urgent',
            field=models.BooleanField(default=False, verbose_name='Urgente'),
        ),
    ]