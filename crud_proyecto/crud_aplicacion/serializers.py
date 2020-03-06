from rest_framework import serializers
from .models import ciudad, municipio, sucursal, producto, inventario, precioProducto, proveedor, pago, tipoSuscripcion, categoria, especialidad
from .models import cliente, empleado, venta, ventaPago, suscripcion, cajero, gerente, sucursal_inventario, venta_Producto, proveedor_Producto
from .models import mejoresEmpleados, mejoresProductos, mejoresSucursales, funcion, historico

class historicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = historico
        fields = ('__all__')

class funcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcion
        fields = ('__all__')

class mejoresProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = mejoresProductos
        fields = ('__all__')

class ciudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudad
        fields = ('id', 'nombre')

class municipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = municipio
        fields = ('id', 'nombre', 'ciudadID')

class municipioAuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = municipio
        fields = ('id', 'nombre', 'ciudadID')
        depth = 1

class sucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = sucursal
        fields = ('id', 'nombre', 'municipioID', 'activo')

class sucursalAuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = sucursal
        fields = ('id', 'nombre', 'municipioID', 'activo')
        depth = 2

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('id', 'nombre')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ('id', 'nombre', 'categoriaID')

class productoAuxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = producto
        fields = ('id', 'nombre', 'categoriaID')
        depth = 1

class funcionSerializer(serializers.ModelSerializer):
    precio = serializers.SerializerMethodField('ultimo_precio')

    def ultimo_precio(self, p):
        return(p.ultimo_precio)
        
    class Meta:
        model = producto
        fields = ('id', 'nombre', 'categoriaID', 'precio')
        depth = 1

class inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventario
        fields = ('id', 'productoID', 'cantidad')

class precioProductoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = precioProducto
        fields = ('productoID', 'monto', 'fecha')

class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = ('id', 'nombre', 'telefono', 'ciudadID', 'activo')

class proveedorAuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = ('id', 'nombre', 'telefono', 'ciudadID', 'activo')
        depth = 1

class pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = ('id', 'monto', 'instrumento')

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('id', 'cedula', 'nombre', 'apellido', 'telefono')

class empleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = ('id', 'cedula', 'nombre', 'apellido', 'fechaNacimiento', 'telefono', 'sucursalID', 'activo')

class empleadoAuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = ('id', 'cedula', 'nombre', 'apellido', 'fechaNacimiento', 'telefono', 'sucursalID', 'activo')
        depth = 1

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = ('id', 'fechaVenta', 'clienteID', 'empleadoID')

class ventaAuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = ('id', 'fechaVenta', 'clienteID', 'empleadoID')
        depth = 1

class ventaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventaPago
        fields = ('ventaID', 'pagoID')

class tipoSuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoSuscripcion
        fields = ('id', 'nombre')

class suscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = suscripcion
        fields = ('id', 'clienteID', 'fechaSuscripcion', 'tipoID', 'activo')

class suscripcionAuxSerializer(serializers.ModelSerializer):
    class Meta:
        model = suscripcion
        fields = ('id', 'clienteID', 'fechaSuscripcion', 'tipoID', 'activo')
        depth = 1

class cajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = cajero
        fields = ('empleadoID', 'nroCaja')

class especialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
        fields = ('id', 'nombre')

class gerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = gerente
        fields = ('empleadoID', 'especialidadID')

class sucursal_inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = sucursal_inventario
        fields = ('sucursalID', 'inventarioID')

class venta_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta_Producto
        fields = ('ventaID', 'productoID', 'cantidad')

class proveedor_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor_Producto
        fields = ('proveedorID', 'productoID')

class mejoresEmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = mejoresEmpleados
        fields = ('__all__')
        depth = 1

class mejoresSucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = mejoresSucursales
        fields = ('__all__')
        depth = 1

