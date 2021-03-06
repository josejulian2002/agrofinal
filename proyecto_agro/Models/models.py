from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    tipousu_id = models.AutoField(primary_key=True)
    tipousu_nom = models.CharField(max_length=50,help_text="Nombre del tipo usuario", unique=True)

    def __str__(self):
        return '{}'.format(self.tipousu_nom)

    class Meta:
        db_table = "t_tipo_usuario"
        verbose_name_plural = "TiposUsuarios"


class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nom = models.CharField(max_length=50,help_text="Nombre de la categoria", unique=True)

    def __str__(self):
        return '{}'.format(self.cat_nom)

    class Meta:
        db_table = "t_categoria"
        verbose_name_plural = "Categorias"


class Almacen(models.Model):
    alma_id = models.AutoField(primary_key=True)
    alma_desc = models.CharField(max_length=50,help_text="Descripcion del almacen", unique=True)

    def __str__(self):
        return '{}'.format(self.alma_desc)

    class Meta:
        db_table = "t_almacen"
        verbose_name_plural = "Almacenes"


class TipoPago(models.Model):
    tipopa_id = models.AutoField(primary_key=True)
    tipopa_nom = models.CharField(max_length=50,help_text="Nombre del tipo de pago", unique=True)
    tipopa_est = models.BooleanField(default=False)
    def __str__(self):
        return '{}'.format(self.tipopa_nom)

    class Meta:
        db_table = "t_tipo_pago"
        verbose_name_plural = "TiposPagos"


class Estado(models.Model):
    est_id = models.AutoField(primary_key=True)
    est_nom = models.CharField(max_length=50,help_text="Nombre del estado de pedido", unique=True)
    def __str__(self):
        return '{}'.format(self.est_nom)

    class Meta:
        db_table = "t_estado"
        verbose_name_plural = "Estados"


class Calificacion(models.Model):
    cal_id = models.AutoField(primary_key=True)
    cal_estr = models.IntegerField(help_text="Estrella de la calificacion el pedido", unique=True)
    def __str__(self):
        return '{}'.format(self.cal_estr)

    class Meta:
        db_table = "t_calificacion"
        verbose_name_plural = "Calificaciones"


class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_mail = models.EmailField(max_length=50, help_text="Email del usuario", unique=True)
    usu_salt = models.TextField(unique=False)
    usu_hash = models.TextField(unique=False)
    usu_nom = models.CharField(max_length=45, help_text="Nombre del usuario", unique=False)
    usu_ape = models.CharField(max_length=50, help_text="Apellido del usuario", unique=False)
    usu_fono = models.CharField(max_length=20, help_text="Telefono del usuario", unique=False)
    tipousu_id = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.usu_nom)
    
    class Meta:
        db_table = "t_usuario"
        verbose_name_plural = "Usuarios"


class Ubicacion(models.Model):
    ubi_id = models.AutoField(primary_key=True)
    ubi_dir = models.CharField(max_length=200, help_text="Direccion de la ubicacion", unique=False)
    ubi_ciudad = models.CharField(max_length=45, help_text="Ciudad de la ubicacion", unique=True)
    ubi_lat = models.DecimalField(max_digits=10, decimal_places=8, help_text="Latitud")
    ubi_lng = models.DecimalField(max_digits=10, decimal_places=8, help_text="Longitud")
    usu_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.ubi_dir)
    
    class Meta:
        db_table = "t_ubicacion"
        verbose_name_plural = "Ubicaciones"

class UsuarioCategoria(models.Model):
    usucat_id = models.AutoField(primary_key=True)
    usu_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_usuario_categoria"
        verbose_name_plural = "UsuariosCategorias"


class Producto(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_nom = models.CharField(max_length=40, help_text="Nombre del producto", unique=False)
    prod_desc = models.CharField(max_length=40, help_text="Descripcion del producto", unique=False)
    cat_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_producto"
        verbose_name_plural = "Productos"


class ImagenProducto(models.Model):
    imgprod_id = models.AutoField(primary_key=True)
    imgprod_url = models.TextField(help_text="URL de la imagen del producto", unique=False)
    prod_id = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.imgprod_url)
    
    class Meta:
        db_table = "t_imagen_producto"
        verbose_name_plural = "ImagenesProductos"


class Presentacion(models.Model):
    pres_id = models.AutoField(primary_key=True)
    pres_est = models.BooleanField(default=False)
    pres_can = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    pres_uni = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    
    class Meta:
        db_table = "t_presentacion"
        verbose_name_plural = "Presentaciones"


class Inventario(models.Model):
    inve_id = models.AutoField(primary_key=True)
    inve_cant = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    alma_id = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pres_id = models.ForeignKey(Presentacion, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_inventario"
        verbose_name_plural = "Inventarios"

class Pedido(models.Model):
    ped_id = models.AutoField(primary_key=True)
    ped_fechin = models.DateTimeField()
    ped_fechfin= models.DateTimeField()
    ped_total = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    est_id = models.ForeignKey(Estado, on_delete=models.CASCADE)
    t_ubicacion_ubi_id = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_pedido"
        verbose_name_plural = "Pedidos"


class PagoPedido(models.Model):
    pagoped_id = models.AutoField(primary_key=True)
    pagoped_url = models.TextField(unique=False)
    pagoped_monto = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    tipopa_id = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    ped_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_pago_pedido"
        verbose_name_plural = "PagosPedidos"


class Precio(models.Model):
    pre_id = models.AutoField(primary_key=True)
    pre_fechin = models.DateTimeField()
    pre_fechfin= models.DateTimeField()
    pre_precio = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    prod_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pres_id = models.ForeignKey(Presentacion, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_precio"
        verbose_name_plural = "Precios"



class DetallePedido(models.Model):
    dped_id = models.AutoField(primary_key=True)
    dped_desc = models.CharField(max_length=100, help_text="Descripcion del detalle de pedido", unique=False)
    dped_subtotal = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    dped_total = models.DecimalField(max_digits=10, decimal_places=2, unique=False)
    dped_nro = models.CharField(max_length=10, unique=False)
    dped_cant = models.DecimalField(max_digits=10, decimal_places=2, unique=False)    
    ped_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pre_id = models.ForeignKey(Presentacion, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_detalle_pedido"
        verbose_name_plural = "DetallePedidos"