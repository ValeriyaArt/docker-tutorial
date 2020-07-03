# Generated by Django 3.0 on 2020-05-25 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=4, verbose_name='Номер кабинета')),
                ('profile', models.CharField(blank=True, choices=[('Для_профильных_дисциплин', 'Для Профильных Дисциплин'), ('Для_базовых_дисциплин', 'Для Базовых Дисциплин')], max_length=100, verbose_name='Тип кабинета')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеты',
            },
        ),
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], max_length=2, verbose_name='Класс')),
                ('litera', models.CharField(blank=True, choices=[('А', 'А'), ('Б', 'Б'), ('В', 'В'), ('Г', 'Г'), ('Д', 'Д'), ('Е', 'Е')], max_length=2, verbose_name='Литера')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Предмет')),
                ('profile', models.CharField(blank=True, choices=[('Профильная_дисциплина', 'Профильная Дисциплина'), ('Базовая_дисциплина', 'Базовая Дисциплина')], max_length=100, verbose_name='Тип предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('teaching_period', models.DateField(verbose_name='Преподает до')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(blank=True, choices=[('1-8:00-8:45', '1-8:00-8:45'), ('2-8:50-9:35', '2-8:50-9:35'), ('3-9:40-10:25', '3-9:40-10:25'), ('4-10:40-11:25', '4-10:40-11:25'), ('5-11:30-12:15', '5-11:30-12:15'), ('6-12:20-13:05', '6-12:20-13:05'), ('7-13:05-13:50', '7-13:05-13:50'), ('8-14:00-14:45', '8-14:00-14:45')], max_length=50, verbose_name='Урок')),
                ('day', models.CharField(blank=True, choices=[('Понедельник', 'Понедельник'), ('Вторник', 'Вторник'), ('Среда', 'Среда'), ('Четверг', 'Четверг'), ('Пятница', 'Пятница'), ('Суббота', 'Суббота')], max_length=100, verbose_name='День недели')),
                ('cabinet_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Cabinet', verbose_name='Кабинет')),
                ('klass_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Klass')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject', verbose_name='Предмет')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Klass')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.AddField(
            model_name='klass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2, verbose_name='Оценка за четверть')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Pupil')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject')),
            ],
            options={
                'verbose_name': 'Четвертная оценка',
                'verbose_name_plural': 'Четвертные оценки',
            },
        ),
        migrations.AddField(
            model_name='cabinet',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
    ]