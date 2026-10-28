import pandas as pd
from pathlib import Path

RUTA_DATOS = Path(__file__).resolve().parent.parent / "Datos-Bi"
datos = pd.read_csv(RUTA_DATOS / "ventas_clientes.csv", sep=";")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print("=== FORMA ===")
print(datos.shape)

print("\n=== PRIMERAS FILAS ===")
print(datos.head(10))

print("\n=== TIPOS (dtypes) ===")
print(datos.dtypes)

print("\n=== FILAS DUPLICADAS ===")
print(datos.duplicated().sum())

print("\n=== VACÍOS POR COLUMNA ===")
print(datos.isna().sum())

print("\n=== ESTADÍSTICAS NUMÉRICAS (min, max...) ===")
print(datos.describe())

print("\n=== VALORES DISTINTOS EN COLUMNAS DE TEXTO ===")
for col in datos.select_dtypes(include="object").columns:
    n = datos[col].nunique()
    print(f"\n--- {col}: {n} valores distintos ---")
    if n <= 40:
        print(datos[col].value_counts(dropna=False))

print("\n=== ESPACIOS SOBRANTES EN TEXTO ===")
for col in datos.select_dtypes(include="object").columns:
    n = (datos[col].dropna() != datos[col].dropna().str.strip()).sum()
    if n:
        print(f"{col}: {n} filas con espacios al inicio o final")
print("\n=== CONTEOS ADICIONALES ===")
print("Cantidades negativas:", (datos["cantidad"] < 0).sum())
print("Precios con $:", datos["precio_unitario"].str.contains(r"\$").sum())

fechas_iso = datos["fecha"].str.match(r"^\d{4}-\d{2}-\d{2}$", na=False).sum()
fechas_barra = datos["fecha"].str.contains("/", na=False).sum()
print("Fechas formato AAAA-MM-DD:", fechas_iso)
print("Fechas formato con /:", fechas_barra)
print("Fechas con otro formato:", datos["fecha"].notna().sum() - fechas_iso - fechas_barra)

print("Categorias distintas sin limpiar:", datos["categoria"].nunique())
print("Categorias distintas tras strip+lower:", datos["categoria"].str.strip().str.lower().nunique())
print("Ciudades distintas sin limpiar:", datos["ciudad_y"].nunique())
print("Ciudades distintas tras strip+lower:", datos["ciudad_y"].str.strip().str.lower().nunique())


