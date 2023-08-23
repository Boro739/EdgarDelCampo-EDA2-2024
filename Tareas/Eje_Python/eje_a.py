def veg(ingredientes):
    while True:
        opcion=int(input("""\t\t\t---Menu Vegetariana---

        (Recuerde que todas las pizzas llevan  mozzarella y el tomate, ademas del ingrediente que va a llevar a continuacion)
    
        Elija que tipo de ingrediente desea
    
        1)  Pimiento
        2)  Tofu
        3)  Regresar
        
        """))

        if opcion==1:
            return ingredientes.append('Pimiento')
        elif opcion==2:
            return ingredientes.append('Tofu')
        elif opcion==3:
            break
        else:
            print("Opcion invalida")

def no_veg(ingredientes):
    while True:
        opcion=int(input("""\t\t\t---Menu No vegetariana---

        (Recuerde que todas las pizzas llevan  mozzarella y el tomate, ademas del ingrediente que va a llevar a continuacion)
    
        Elija que tipo de ingrediente desea
    
        1)  Peperoni
        2)  Jamon
        3)  Salmon
        4)  Regresar
        
        """))

        if opcion==1:
            return ingredientes.append('Peperoni')
        elif opcion==2:
            return ingredientes.append('Jamon')
        elif opcion==3:
            return ingredientes.append('Salmon')
        elif opcion==4:
            break
        else:
            print("Opcion invalida")




#####Pricipal#####

ingredientes=['mozzarella', 'tomate']

while True:

    print("")
    
    opcion=int(input("""\t\t\t---Bienvenido a la pizzería Bella Napoli---
    
    Elija que tipo de pizza le gustaria
    
    1) Vegetariana
    2) No vegetariana
    3) Salir
    
    """))

    if opcion==1:
        veg(ingredientes)
        print(f"""///Confirmando su pedido///
        
        Su pizza es vegetariana y sus ingredientes son:
        {ingredientes[0]}
        {ingredientes[1]}
        {ingredientes[2]}""")
        print("Gracias vuelva pronto")
        break

    elif opcion==2:
        no_veg(ingredientes)
        print(f"""///Confirmando su pedido///
        
        Su pizza es no es vegetariana y sus ingredientes son:
        {ingredientes[0]}
        {ingredientes[1]}
        {ingredientes[2]}""")
        print("Gracias vuelva pronto")
        break

    elif opcion==3:
        print("Gracias vuelva pronto")
        break
    else:
        print("Opcion invalida")
        
