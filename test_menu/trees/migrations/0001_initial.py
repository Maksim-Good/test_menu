# Generated by Django 2.2.19 on 2023-03-29 09:01

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название меню')),
            ],
        ),
        migrations.CreateModel(
            name='ChieldMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chield_name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chield_name', to='trees.Menu', verbose_name='Меню')),
                ('father_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father_name', to='trees.Menu', verbose_name='Отец')),
            ],
        ),
        migrations.AddConstraint(
            model_name='chieldmenu',
            constraint=models.UniqueConstraint(fields=('chield_name', 'father_name'), name='unique_parrents'),
        ),
        migrations.AddConstraint(
            model_name='chieldmenu',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, chield_name=django.db.models.expressions.F('father_name')), name='self_father'),
        ),
    ]
