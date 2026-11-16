# Statistical Physics and Financial Markets

Projeto educacional e exploratório que combina Física Estatística, Econofísica, Matemática Aplicada e Ciência de Dados para investigar propriedades de séries temporais financeiras.

## Objetivos
- Calcular e analisar retornos simples e logarítmicos.
- Investigar distribuições, volatilidade e correlações.
- Estudar medidas de incerteza, incluindo entropia de Shannon.
- Implementar experimentos de processos estocásticos e Monte Carlo.
- Explorar o modelo de Ising como analogia física, explicitando suas limitações.

## Estrutura
- `notebooks/`: desenvolvimento didático e análises documentadas.
- `src/`: funções Python reutilizáveis.
- `tests/`: testes automatizados.
- `data/raw/`: dados originais locais (ignorados pelo Git).
- `data/processed/`: dados tratados locais (ignorados pelo Git).
- `figures/`: figuras geradas (ignoradas pelo Git).

## Configuração no Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

No VS Code, instale as extensões Python e Jupyter e selecione o kernel do ambiente `.venv`.

## Testes
Na raiz do projeto:
```powershell
python -m pytest
```

## Reprodutibilidade e responsabilidade
Registre fonte, período, frequência, parâmetros e tratamento dos dados. Verifique a licença e os termos de uso da fonte antes de redistribuir dados. O projeto é para fins educacionais e de pesquisa exploratória; não oferece recomendações de investimento. Correlação não implica causalidade, e modelos simplificados não devem ser interpretados como previsores confiáveis sem validação rigorosa.

## Etapas
1. Fundamentação matemática.
2. Coleta e tratamento.
3. Análise exploratória.
4. Distribuições.
5. Volatilidade e correlações.
6. Entropia.
7. Processos estocásticos.
8. Monte Carlo.
9. Modelo de Ising.
10. Conclusões.
