from collections import Counter
import copy as copy
import datetime as datetime

class Pizza():
    def __init__(self, tamano='', nombre='', tipo='', ingredientes=[], precio=0):
        self.tamano = tamano
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.ingredientes = ingredientes
    def tamano_(self, a):
        self.tamano = a
    def nombre_(self, a):
        self.nombre = a
    def tipo_(self, a):
        self.tipo = a        
    def precio_(self, a):
        self.precio = a
    def ingredientes_(self, lista):
        self.ingredientes = lista.copy()
    def calcular_precio_tipo(self, precio):
        if pizza_1.tamano == '8 porciones':
            return precio * 8
        if pizza_1.tamano == '10 porciones':
            return precio * 10
        if pizza_1.tamano == '12 porciones':
            return precio * 12
    def __eq__(self, obj1):
        return (self.tamano == obj1.tamano) and (self.nombre == obj1.nombre) and (self.tipo == obj1.tipo)
    def mostrar(self):
        print(f'{self.nombre} de {self.tamano} de tipo {self.tipo}', end = ' ')                  

class Todas():
    def __init__(self, pizzas=[]):
        self.pizzas = pizzas
    def mas_comun(self):
        counter = 0
        num = Pizza()
        num = self.pizzas[0]
        for y in self.pizzas:
            curr_frequency = self.pizzas.count(y)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = y
    
        return num
# class Periodos():
#     def __init__(self):


class Pedido():
    def __init__(self, nombre='', cantidad=0, pizzas=[]):
        self.nombre = nombre
        self.cantidad = cantidad
        self.pizzas = pizzas
    def mostrar_factura(self):
        precio_1 = 0
        print('Su factura:')
        for y in self.pizzas:
            precio_1 += y.precio 
            print(f'{y.nombre} de {y.tamano} de tipo {y.tipo} - {y.precio} $')
        print(f'Total a pagar {precio_1}')    
    
class Pedidos_totales():
    def __init__(self, lista=[], cantidad=0):
        self.lista = lista
        self.cantidad = cantidad
    def agregar(self, lista):
        self.lista.append(lista)
    def mostrar(self):
        for x in self.lista:
            print(f'Pizzas pedidas por {x.nombre}:')
            for y in x.pizzas:
                print(y.nombre)

class Cliente():
    def __init__(self, nombre=''):
        self.nombre = nombre
        ################        
lista_1 = Pedidos_totales()
pedido_1 = Pedido()
pizza_1 = Pizza()
todas_1 = Todas()
        ################
while True:
    print('----------MENU----------')
    print('------------------------')
    print('Su nombre por favor para hacer el pedido')
    print('------------------------')
    print('A - terminar programa')
    print('------------------------')
    print('B - lista de todos los pedidos con nombre')
    print('C - Pizza mas comun pedida por los clientes')
    a = input('')
    if a.lower() == 'a':
        break
    elif a.lower() == "b":
        lista_1.mostrar()
    elif a.lower() == 'c':
        pizza_1 = todas_1.mas_comun()
        pizza_1.mostrar()
        print('es la pizza mas pedida por los clientes')
    else:
        pedido_1.nombre = a
        while True:
            print('----------MENU----------')
            print('------------------------')
            print('A - Agregar pizza al pedido ')
            print('B - Terminar pedido')
            a = input('')
            if a.lower() == 'b':
                break
            elif a.lower() == 'a':
                while True:
                    print('----------MENU----------')
                    print('------------------------')
                    print('Eliga el tamano de su pizza')
                    print('')
                    print('A - 8 porciones')
                    print('B - 10 porciones')
                    print('C - 12 porciones')
                    print('------------------------')
                    a = input('')
                    if a.lower() == 'a':
                        a = '8 porciones'
                        pizza_1.tamano_(a)
                        break 
                    elif a.lower() == 'b':
                        a = '10 porciones'
                        pizza_1.tamano_(a)
                        break
                    elif a.lower() == 'c':
                        a = '12 porciones'
                        pizza_1.tamano_(a)
                        break
                    else:
                        print('Dato mal ingresado')
                while True:
                    print('----------MENU----------')
                    print('------------------------')
                    print('Eliga cual pizza quiere')
                    print('')
                    print('A - Muzza (queso y masa)')
                    print('B - Nappo (queso, masa y tomate')
                    print('C - 4 quesos (queso1, queso2, queso3 y queso4')
                    print('------------------------')
                    a = input('')
                    if a.lower() == 'a':
                        a = 'Muzza'
                        b = ['queso', 'masa']
                        pizza_1.nombre_(a)
                        pizza_1.ingredientes_(b)
                        break 
                    elif a.lower() == 'b':
                        a = 'Nappo'
                        b = ['queso', 'masa', 'tomates']
                        pizza_1.nombre_(a)
                        pizza_1.ingredientes_(b)
                        break
                    elif a.lower() == 'c':
                        a = '4 quesos'
                        b = ['queso1', 'queso2', 'queso3', 'queso4']
                        pizza_1.nombre_(a)
                        pizza_1.ingredientes_(b)
                        break
                    else:
                        print('Dato mal ingresado')
                while True:
                    print('----------MENU----------')
                    print('------------------------')
                    print('Eliga el tipo de pizza quiere')
                    print('')
                    print('A - A la piedra')
                    print('B - A la parrilla')
                    print('C - De molde')
                    print('------------------------')
                    a = input('')
                    if a.lower() == 'a':
                        a = "a la piedra"
                        pizza_1.tipo_(a)
                        break 
                    elif a.lower() == 'b':
                        a = 'a la parrilla'
                        pizza_1.tipo_(a)
                        break
                    elif a.lower() == 'c':
                        a = 'de molde'
                        pizza_1.tipo_(a)
                        break
                    else:
                        print('Dato mal ingresado')
                
                if pizza_1.tipo == 'a la piedra':
                    precio = 10
                    pizza_1.precio_(pizza_1.calcular_precio_tipo(precio))
                elif pizza_1.tipo == 'a la parrilla':
                    precio = 12
                    pizza_1.precio_(pizza_1.calcular_precio_tipo(precio))                 
                elif pizza_1.tipo == 'de molde':
                    precio = 15
                    pizza_1.precio_(pizza_1.calcular_precio_tipo(precio))   
                
                pedido_1.cantidad += 1
                pedido_1.pizzas.append(copy.deepcopy(pizza_1))
                todas_1.pizzas.append(copy.deepcopy(pizza_1))
            else:
                print('Dato mal ingresado')
        
        print(f'Se le informa a {pedido_1.nombre} que su pedido fue tomado ')
        pedido_1.mostrar_factura()
        print('Ingrese cualquier caracter para volver al menu principal')
        input('')
        lista_1.lista.append(copy.deepcopy(pedido_1))
        pedido_1.pizzas = []
        pedido_1.cantidad = 0

    




                 
            
