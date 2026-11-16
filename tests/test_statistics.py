import numpy as np
import pandas as pd
import pytest

from src.statistical_analysis import calcular_retornos, estatisticas_retornos


def test_quantidade_de_retornos():
    precos = pd.Series([100, 102, 101, 105])
    resultado = calcular_retornos(precos)
    assert len(resultado) == 3


def test_retorno_simples_manual():
    precos = pd.Series([100, 102])
    resultado = calcular_retornos(precos)
    assert np.isclose(resultado["simples"].iloc[0], 0.02)


def test_retorno_logaritmico_manual():
    precos = pd.Series([100, 102])
    resultado = calcular_retornos(precos)
    assert np.isclose(resultado["logaritmico"].iloc[0], np.log(1.02))


def test_rejeita_preco_nao_positivo():
    with pytest.raises(ValueError):
        calcular_retornos(pd.Series([100, 0, 102]))


def test_estatisticas():
    retornos = pd.Series([0.01, 0.02, -0.01])
    resultado = estatisticas_retornos(retornos)
    assert resultado["quantidade"] == 3
    assert np.isclose(resultado["media"], retornos.mean())
