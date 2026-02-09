from empleado_modelo import empleado_modelo
from diccionarios import datos_diccionario
from Base_datos_empleados import Base_datos_empleados

obj_diccionario = datos_diccionario()
info = obj_diccionario.sacar_elementos()
print(info)

nuevo_diccionario = {"1098674567": {"Nombre: " "Juan", "Apellido: " "Pérez", "Máquina: " ("Máquina pinturas", "Máquina hidráulica")}}

obj_diccionario.actualizar_info(nuevo_diccionario)
obj_diccionario.imprimir_info() 