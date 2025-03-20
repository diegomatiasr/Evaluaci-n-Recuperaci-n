import pandas as pd
import numpy as np
import os

def cargar_archivo(ruta):
    extension = os.path.splitext(ruta)[-1].lower()
    
    if extension == ".csv":
        return pd.read_csv(ruta)
    elif extension == ".html":
        return pd.read_html(ruta)[0]
    else:
        raise ValueError(f"Hola, acabas de ingresar un documento que desconozco, con extensión: {extension}")

def sustituir_nulos(df):
    columnas = df.columns
    es_primo = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    
    for i, col in enumerate(columnas):
        if df[col].dtype in [np.float64, np.int64]:
            df[col].fillna(1111111 if es_primo(i) else 1000001, inplace=True)
        else:
            df[col].fillna("Valor Nulo", inplace=True)
    
    return df

def identificar_nulos(df):
    nulos_por_columna = df.isnull().sum()
    nulos_totales = df.isnull().sum().sum()
    
    return {"nulos_por_columna": nulos_por_columna, "nulos_totales": nulos_totales}