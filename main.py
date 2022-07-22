from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        menu = """
        Seleccione los detalles que desea ver
        1.-Rectangulo
        2.-Circulo
        3.- Salir
        Ingresa aqui tu opción: """

        opcion = input(menu)
        
        if opcion == '1':
            base = float(input('Ingrese Base: '))
            altura = float(input('Ingrese Altura: '))
            r = Rectangulo(base, altura)
            probar_figura(r)
            #print(r)                  
        elif opcion == '2':
            radio = float(input('Ingrese Radio: '))
            c = Circulo(radio)
            probar_figura(c)
            #print(c)  
        elif opcion == '3':
            print('saliendo del sistema')
            break
        else:
            print('Debes ingresar una de las opciones en pantalla.')           

if __name__ == '__main__':
    main()