# Reto_semana_03_David_Emiliano
# Analizador de Ventas Transaccionales (Reto Semana 3)

## Programación para Ciencia de Datos | IPN - ESCOM
**Estudiante:** David Emiliano Rodríguez Anduiza  
**Institución:** Instituto Politécnico Nacional  
**Semestre:** Febrero - Julio 2026

---

## Analizador de Ventas Escalable en Python
Este proyecto implementa una solución de procesamiento de datos tipo ETL (Extract, Transform, Load) diseñada para la consolidación de flujos de transacciones masivas.

## Objetivo del Proyecto
Desarrollar un sistema robusto capaz de consumir datos crudos desde la entrada estándar (stdin), realizar agregaciones financieras complejas mediante estructuras de datos optimizadas y generar reportes consolidados bajo estándares de industria.

## Arquitectura de la Solución
El programa emplea un diseño de procesamiento lineal para garantizar la eficiencia en el consumo de memoria, manteniendo una complejidad temporal de O(n). Esto resulta fundamental al trabajar con conjuntos de datos que exceden la capacidad de la memoria RAM.

## 1. Extracción y Limpieza de Datos (Data Scrubbing)
El script procesa la información línea por línea, realizando las siguientes validaciones de integridad:
Validación Estructural: Filtra registros que no cumplen con el formato de cuatro columnas requerido.
Conversión de Tipos: Implementa manejo de excepciones para la transformación de datos (int para unidades y float para precios) mediante bloques try-except.

## 2.Transformación y Agregación
Se utiliza un diccionario anidado para realizar el agrupamiento de datos. Esta estructura permite operaciones de búsqueda y actualización en tiempo constante O(1).

## 3. Gestión de Errores Matemáticos: El Desafío del Valor Infinito
Durante la fase de pruebas con datasets de estrés, se detectaron desbordamientos de punto flotante (floating-point overflow) que resultaban en valores "inf" (infinitos).
- Problema: Valores excesivamente altos en el cálculo de (cantidad * precio) corrompían el ingreso total y el precio promedio.
- Solución: Se integró el módulo math para verificar la finitud de cada cálculo antes de su almacenamiento. Mediante la función math.isinf(), se identifican y descartan registros corruptos o fuera de rango (outliers), asegurando la integridad del reporte final.

## Especificaciones Técnicas
## Componente: Función Principal
- sys:Gestión de flujos de entrada/salida (stdin/stdout) para integración en pipelines.
- math: Validación de integridad numérica y detección de desbordamientos de memoria.
- sorted: Aplicación del algoritmo Timsort para el ordenamiento de rentabilidad.             

## Lógica de Ordenamiento
El reporte se genera transformando el diccionario de productos en una lista de objetos, la cual se ordena mediante una función lambda referenciada al ingreso total en orden descendente.

# Núcleo del algoritmo de ordenamiento
reporte_ordenado = sorted(reporte, key=lambda x: x["ingreso"], reverse=True)

## Guía de Ejecución
Debido a las restricciones de operadores en entornos PowerShell, se recomienda la ejecución mediante el uso de tuberías (pipes).

## Comandos de Terminal
## - Clonación del Repositorio:
git clone https://github.com/emi-roan/Reto_semana_03_David_Emiliano.git
cd Reto_semana_03_David_Emiliano

## - Procesamiento de Datos en PowerShell:
Get-Content test/entrada.txt | python main.py

## - Redirección a Reporte Físico:
Get-Content test/entrada.txt | python main.py > test/reporte_final.csv

Casos de Prueba Implementados
Datos Inconsistentes: El sistema ignora automáticamente cadenas de texto en columnas de valor numérico.
Manejo de Overflow: Detección y exclusión de valores astronómicos que comprometen la precisión del reporte.
Registros Incompletos: Omisión de líneas con formatos inválidos o saltos de línea huérfanos.
