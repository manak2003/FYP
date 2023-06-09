# Generated by Django 4.1.1 on 2023-04-08 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_alter_membership_membership_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='stripe_subscription_id',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='stripe_customer_id',
        ),
        migrations.AddField(
            model_name='membership',
            name='duration',
            field=models.PositiveIntegerField(default=7),
        ),
        migrations.AddField(
            model_name='membership',
            name='duration_period',
            field=models.CharField(choices=[('Days', 'Days'), ('Week', 'Week'), ('Months', 'Months '), ('Year', 'Year')], default='Days', max_length=30),
        ),
        migrations.AddField(
            model_name='subscription',
            name='expires_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.CharField(choices=[('Extended', 'Extended'), ('Advance', 'Advance'), ('Medium', 'Medium'), ('Basic', 'Basic'), ('Free', 'Free')], default='Free', max_length=30),
        ),
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='membership',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user_membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscription', to='members.usermembership'),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_membership', to='members.membership'),
        ),
        migrations.CreateModel(
            name='UserSettingz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_verified', models.BooleanField(default=False)),
                ('verified_code', models.CharField(blank=True, max_length=10, null=True)),
                ('code_expired', models.BooleanField(default=False)),
                ('recieve_email_notice', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_for', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_membership', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
