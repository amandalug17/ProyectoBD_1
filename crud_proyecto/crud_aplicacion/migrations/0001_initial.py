# Generated by Django 3.0.2 on 2020-03-02 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
            },
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(default='', unique=True)),
                ('nombre', models.CharField(max_length=400)),
                ('apellido', models.CharField(max_length=400)),
                ('telefono', models.CharField(default='', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(default='', unique=True)),
                ('nombre', models.CharField(max_length=400)),
                ('apellido', models.CharField(max_length=400)),
                ('fechaNacimiento', models.CharField(default='', max_length=12)),
                ('telefono', models.CharField(default='', max_length=12)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
                ('ciudadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, default='', max_digits=10)),
                ('instrumento', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
                ('categoria', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
                ('telefono', models.CharField(default='', max_length=15)),
                ('activo', models.BooleanField(default=True)),
                ('ciudadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.ciudad')),
            ],
            options={
                'verbose_name': 'proveedor',
                'verbose_name_plural': 'proveedores',
            },
        ),
        migrations.CreateModel(
            name='sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
                ('activo', models.BooleanField(default=True)),
                ('municipioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.municipio')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaVenta', models.DateTimeField(auto_now_add=True)),
                ('clienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.cliente')),
                ('empleadoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='ventaPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.pago')),
                ('ventaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.venta')),
            ],
        ),
        migrations.CreateModel(
            name='venta_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default='')),
                ('productoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.producto')),
                ('ventaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.venta')),
            ],
        ),
        migrations.CreateModel(
            name='suscripcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaSuscripcion', models.DateField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=400)),
                ('activo', models.BooleanField(default=True)),
                ('clienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.cliente')),
            ],
            options={
                'verbose_name': 'suscripcion',
                'verbose_name_plural': 'suscripciones',
            },
        ),
        migrations.CreateModel(
            name='sucursal_inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventarioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.inventario')),
                ('sucursalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='proveedor_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.producto')),
                ('proveedorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='precioProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, default='', max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('productoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='productoID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.producto'),
        ),
        migrations.CreateModel(
            name='gerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=400)),
                ('empleadoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.empleado')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursalID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.sucursal'),
        ),
        migrations.CreateModel(
            name='cajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroCaja', models.PositiveIntegerField(default='')),
                ('empleadoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_aplicacion.empleado')),
            ],
        ),
    ]
