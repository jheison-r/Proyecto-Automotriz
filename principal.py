from empleado_modelo import empleado_modelo
from Bdatos import Api_BD
#codigo principal
obj_Api = Api_BD()
obj_empleado=Epleado_modelo("jheison","ramirez","934723894","321-273982")

obj_Api.guardar_empleado(obj_empleado)
print(obj_empleado)
print(obj_empleado.ver_infor())


obj_Api_maquina = Api_BD_maquinas()
obj_Api_maquina.imprimir_info()
obj_Api.guardar_empleado(obj_empleado)
obj_Api.imprimir_Api()