def amor():
    cantidad_amor = input("cuanto me amas: ")
    try:
        cantidad_amor = int(cantidad_amor)
        print(f"Te amo {cantidad_amor*2}")
    except:
        print("Eso no es un numero")
amor()
