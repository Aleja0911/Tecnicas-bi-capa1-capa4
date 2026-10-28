import pandas as pd
from pathlib import Path

# Carpeta del proyecto (un nivel arriba de Capa_1_Origenes) + Datos-Bi
RUTA_DATOS = Path(__file__).resolve().parent.parent / "Datos-Bi"

# Lectura de ventas
df_ventas = pd.read_excel(RUTA_DATOS / "ventas.xlsx")

# Lectura de clientes
df_clientes = pd.read_csv(RUTA_DATOS / "clientes.csv", sep=";")

print("Filas y columnas ventas:", df_ventas.shape)
print("Filas y columnas clientes:", df_clientes.shape)

print(df_ventas.columns.tolist())
print(df_clientes.columns.tolist())

# Unión (ajusta "id_cliente" a la columna que tengan en común)
df_union = df_ventas.merge(df_clientes, on="id_cliente", how="left")

print("Filas ventas antes de unir:", len(df_ventas))
print("Filas clientes:", len(df_clientes))
print("Filas después de unir:", len(df_union))

df_union.to_csv(RUTA_DATOS / "ventas_clientes.csv", index=False, sep=";", encoding="utf-8-sig")

# ---------------------------------------------------------------
# RESPUESTAS
# 1. ventas.xlsx tiene X filas y Y columnas; clientes.csv tiene X filas y Y columnas
#    (copia aquí los valores que imprime .shape).
# 2. pd.read_csv("datos/clientes.csv") sin sep usa la coma como separador por
#    defecto. Si el archivo usa ";", todo queda en UNA sola columna con los
#    datos pegados (o da ParserError).
# 3. El separador real es ";". Me di cuenta al imprimir df_clientes.head() y ver
#    una sola columna, y al abrir el CSV como texto y ver los ";" entre valores.
# 4. Se unen por la columna "id_cliente" (la que aparece en ambas tablas).
# 5. Usé "left" para conservar todas las ventas, aunque un cliente no
#    aparezca en clientes.csv (no queremos perder ventas).
# 6. Ventas tenía X filas antes de unir y quedaron Y después.
# 7. Si cambió: porque hay clientes duplicados en clientes.csv (una venta se
#    repite por cada coincidencia). Si no cambió, no hay duplicados.
# ---------------------------------------------------------------
