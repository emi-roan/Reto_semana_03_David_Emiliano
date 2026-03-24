import sys

def main():
    productos = {}
    primera_linea = True
    
    for linea in sys.stdin:
        linea = linea.strip()
        
        if primera_linea:
            primera_linea = False
            continue
        
        if not linea:
            continue
        
        partes = linea.split(',')
        if len(partes) != 4:
            continue
        
        producto = partes[1]
        
        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
        except ValueError:
            continue
        
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }
        
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio
    
    lista_productos = []
    for nombre, datos in productos.items():
        unidades = datos["unidades"]
        ingreso = datos["ingreso"]
        promedio = ingreso / unidades if unidades > 0 else 0
        lista_productos.append((nombre, unidades, ingreso, promedio))
    
    lista_ordenada = sorted(lista_productos, key=lambda x: x[2], reverse=True)
    
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for prod in lista_ordenada:
        print(f"{prod[0]},{prod[1]},{prod[2]:.2f},{prod[3]:.2f}")

if __name__ == "__main__":
    main()