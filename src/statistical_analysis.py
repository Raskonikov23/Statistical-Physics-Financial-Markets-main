"""Funções básicas para análise de retornos financeiros."""

import numpy as np
import pandas as pd


def calcular_retornos(precos: pd.Series) -> pd.DataFrame:
    """Calcula retornos simples e logarítmicos a partir de preços positivos.

    A série deve estar ordenada cronologicamente e conter preços numéricos.
    """
    if not isinstance(precos, pd.Series):
        raise TypeError("precos deve ser uma pandas.Series")

    precos = pd.to_numeric(precos, errors="raise")

    if precos.dropna().empty:
        raise ValueError("A série de preços está vazia.")

    if (precos.dropna() <= 0).any():
        raise ValueError("Todos os preços válidos devem ser positivos.")

    retornos = pd.DataFrame(index=precos.index)
    retornos["simples"] = precos.pct_change()
    retornos["logaritmico"] = np.log(precos / precos.shift(1))
    return retornos.dropna()


def estatisticas_retornos(retornos: pd.Series) -> pd.Series:
    """Retorna estatísticas descritivas básicas de uma série de retornos."""
    retornos = pd.to_numeric(retornos, errors="raise").dropna()
    if retornos.empty:
        raise ValueError("Não há retornos válidos para analisar.")

    return pd.Series({
        "quantidade": retornos.count(),
        "media": retornos.mean(),
        "variancia_amostral": retornos.var(),
        "desvio_padrao_amostral": retornos.std(),
        "minimo": retornos.min(),
        "maximo": retornos.max(),
    })


if __name__ == "__main__":
    precos = pd.Series([100, 102, 101, 105, 108, 106, 110])
    resultado = calcular_retornos(precos)
    print("Retornos:")
    print(resultado)
    print("\\nEstatísticas dos retornos logarítmicos:")
    print(estatisticas_retornos(resultado["logaritmico"]))
