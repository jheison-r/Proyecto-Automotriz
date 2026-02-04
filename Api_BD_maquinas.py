class Api_maquinas:
    def __init__(self):
        self.Api_maquina = [
            ["codigo","nombre","modelo maquina","estado maquina"],
            ["cod 1234","brazo mecanico","x200","apagada"],
            ["cod 2345","cinta transportadora","zx400","requiere mantenimiento"],
        ]
    
    def guardar_maquina(self,obj_nueva_maquina):
        self.Api_datos.append(obj_nueva_maquina)

    def imprimir_info(self):
        for i in range(len(self.Api_maquinas)):
            print(self.Api_maquinas[i])
    
    def buscar_info(self):
        return self.Api_maquinas[0][1]
