from Base_datos_empleados import base_datos_empleados
from empleado_modelo3 import Empleado_modelo

#creo la base de datos de empleados 
obj_db_empleados_lista = base_datos_empleados()
#creo el objeto empleado que voy guardar
obj_empleado = Empleado_modelo("jheison", "ramirez", "534535", "321-4582354")
obj_empleado2 = Empleado_modelo("carlos", "perez", "658977", "320-876387638")



listas_nuevos_empleados= (obj_empleado,obj_empleado2)

obj_db_empleados_lista.guardar_empleado(obj_empleado)
obj_db_empleados_lista.guardar_empleado(obj_empleado2)


obj_db_empleados_lista.extender_varios_empleados(listas_nuevos_empleados)

obj_db_empleados_lista.imprimir_info()