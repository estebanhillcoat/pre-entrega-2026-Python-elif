productos = ["pilas","cabsha","5"]

while True:
    
    opcion = input("L - Para listar\nB - Para Buscar\nR - Para Remover\nA - Para Agregar\nQ - para Quitar\n------------------\nS - Para salir\n\n")
    
    if opcion == "S":
        break
    
    elif opcion == "L":
        print(productos)
    
    elif opcion == "A":
        agregar = input("Producto a agregar: \n")
        productos.append(agregar)
        print(f"\n{agregar} se ha agregado con exito!\n")
        
    elif opcion == "R":
        remover = input("Producto a remover: \n")
        productos.remove(remover)
        print(f"\n{remover} se ha removido con exito!\n")

    elif opcion == "B":
        buscar = input("Producto a buscar: \n")
        if buscar in productos:
            print("\nHay stock!\n")
        else:
            print(f"\nNo hay stock de {buscar}\n")
        


