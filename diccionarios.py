class datos_diccionario:
    def __init__(self):
        self.datos_diccionario = {}
        
    def longitud_diccionario(self):
        longitud = len(self.datos_diccionario)
        return
    
    def limpiar_diccionario(self):
        limpiar = self.datos_diccionario.clear()
        return limpiar
    
    def copiar_diccionario(self):
        copiar = self.datos_diccionario.copy()
        return copiar
    
    def sacar_elementos(self):
        sacar = self.datos_diccionario.items()
        return sacar
    
    def devolver_valor(self):
        devolver=self.datos_diccionario.keys()
        return devolver
        
    def eliminar_info(self):
        eliminar = self.datos_diccionario.pop()
        return eliminar
    
    def eliminar_elemento(self): 
        eliminar = self.datos_diccionario.popitem()
        return eliminar

    def actualizar_info(self):
        actualizar = self.datos_diccionario.update()
        return actualizar
    
    def actualizar_info(self, nuevo_diccionario):
        self.datos_diccionario.update(nuevo_diccionario)
        
    def imprimir_info(self):
        for clave in self.datos_diccionario.keys():
            print(f"Dato info:  {self.datos_diccionario[clave]}")