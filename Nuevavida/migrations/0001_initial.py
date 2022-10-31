# Generated by Django 4.0.6 on 2022-10-07 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPago', models.DateField(null=b'I01\n')),
                ('totalDeuda', models.IntegerField(null=b'I01\n')),
                ('totalPago', models.IntegerField(null=b'I01\n')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePlan', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('caracteristicas', models.CharField(max_length=1000, null=b'I01\n')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(blank=True, max_length=250, null=True)),
                ('fechaNacimiento', models.DateField()),
                ('deuda', models.IntegerField(default=0, null=True)),
                ('password', models.CharField(max_length=500)),
                ('rol', models.CharField(choices=[(1, 'administrador'), (2, 'cotizante')], default=2, max_length=20)),
                ('idplan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Nuevavida.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('fechaPago', models.DateField()),
                ('cuota', models.IntegerField()),
                ('cedulaUsuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Nuevavida.usuario')),
                ('idFactura', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Nuevavida.factura')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedulaBeneficiario', models.IntegerField(unique=True)),
                ('nombreBeneficiario', models.CharField(max_length=100)),
                ('apellidoBeneficiario', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('cedulaUsuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Nuevavida.usuario')),
            ],
        ),
    ]
