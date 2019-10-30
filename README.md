# Movelets-genetic-algorithm

Foobar is a Python library for dealing with word pluralization.
Este projeto é a implementação de TCC realizada por Daniel Kock com foco na criação de um novo método de classificação de trajetórias por meio de Algoritmo Genético

## Instalação

Utilize o gerenciador de pacotes do Python [pip](https://pip.pypa.io/) para instalar as dependências do projeto.

```bash
pip install -R requirements.txt
```

## Utilização

Para executar o programa, utilize o comando:

```bash
python main.py
```

Todos os parâmetros de execução são definidos neste arquivo, basta alterá-los e executar novamente o programa

```python

score, time = engine.run(
    EXPERIMENTAL='E2', # { E1(holdout), E2(cross-validation) }
    DATASET_NAME='1_patel_hurricane_2vs3', # { 1_patel_hurricane_2vs3, 2_patel_hurricane_1vs4, 3_patel_hurricane_0vs45, 4_patel_animals, 5_patel_vehicle }
    CLASSIFICATOR='Bayes', # { Bayes, C45, SVM }
    INDIVIDUAL_SIZE=8,
    POPULATION_SIZE=10,
    ELITE_SIZE=1,
    MUTATION_RATE=0.1,
    MUTATION_MULT_FACTOR=2,
    MUTATION_NOT_CONVERGENCE_LIMIT=0,
    NOT_CONVERGENCE_LIMIT=0,
    SELECTION_METHOD='tournament', # { tournament, roullete }
    GENERATIONS=40,
    MOVELET_MIN_SIZE=2,
    MOVELET_MAX_SIZE=3
)

```

No final da execução, o resultado da classificação é impresso na tela, e o gráfico de ganho de acurácia da execucão é salvo na pasta `/results` 

## Contribuição
Pull requests são bem vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)