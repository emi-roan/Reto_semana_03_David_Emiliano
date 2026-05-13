import sys
import math

def main():
    productos = {}
    primera_linea = True
    
    for linea in sys.stdin:
        linea = linea.strip()
        if not linea:
            continue
            
        partes = linea.split(',')
        if len(partes) != 4:
            continue
            
        if primera_linea:
            primera_linea = False
            if "producto" in partes[1].lower() or "fecha" in partes[0].lower():
                continue

        nombre_prod = partes[1].strip()
        
        try:
            cantidad = int(partes[2])
            precio_u = float(partes[3])
            
            # Validación extra: si el precio es una locura, lo saltamos
            ingreso_parcial = cantidad * precio_u
            if math.isinf(ingreso_parcial):
                continue
                
        except ValueError:
            continue
            
        if nombre_prod not in productos:
            productos[nombre_prod] = {"unidades": 0, "ingreso": 0.0}
            
        productos[nombre_prod]["unidades"] += cantidad
        productos[nombre_prod]["ingreso"] += ingreso_parcial

    reporte = []
    for nombre, datos in productos.items():
        u = datos["unidades"]
        ingreso = datos["ingreso"]
        
        # Si por alguna razón la suma total dio infinito, lo ignoramos
        if math.isinf(ingreso):
            continue
            
        promedio = ingreso / u if u > 0 else 0.0
        
        reporte.append({
            "nombre": nombre,
            "unidades": u,
            "ingreso": ingreso,
            "promedio": promedio
        })

    # Ordenar por ingreso descendente
    reporte_ordenado = sorted(reporte, key=lambda x: x["ingreso"], reverse=True)

    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for p in reporte_ordenado:
        print(f"{p['nombre']},{p['unidades']},{p['ingreso']:.2f},{p['promedio']:.2f}")

if __name__ == "__main__":
    main()
