import django.utils.timezone
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=120)),
                ('completeName', models.CharField(max_length=150, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('phone', models.CharField(max_length=11, null=True, blank=True)),
                ('password', models.CharField(max_length=128)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(null=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(
                    blank=True,
                    related_name='user_set',
                    related_query_name='user',
                    to='auth.Group',
                    verbose_name='groups',
                    help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
                )),
                ('user_permissions', models.ManyToManyField(
                    blank=True,
                    related_name='user_set',
                    related_query_name='user',
                    to='auth.Permission',
                    verbose_name='user permissions',
                    help_text='Specific permissions for this user.'
                )),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('street', models.TextField()),
                ('number', models.CharField(max_length=20)),
                ('neighborhood', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.user')),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
    ]