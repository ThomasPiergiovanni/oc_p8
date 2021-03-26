# Generated by Django 3.1.7 on 2021-03-26 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_origin', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('nutriscore_grade', models.CharField(max_length=8)),
                ('fatty_acids', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('saturated_fatty_acids', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('sugar', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('salt', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('image', models.URLField(null=True)),
                ('url', models.URLField(null=True)),
                ('relation_user', models.ManyToManyField(through='supersub.Favorites', to='authentification.User')),
            ],
        ),
        migrations.AddField(
            model_name='favorites',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supersub.product'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.user'),
        ),
    ]
