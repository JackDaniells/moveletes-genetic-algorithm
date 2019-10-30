import engine

import datetime

# E1/E2
# 0 = 1_patel_hurricane_2vs3
# 1 = 2_patel_hurricane_1vs4
# 2 = 3_patel_hurricane_0vs45
# 3 = 4_patel_animals
# 4 = 5_patel_vehicle

# E3
# 1_geolife70

TYPE_CALC = 'max'
RUNTIMES = 1


score = 0
time = 0
for i in range(0, RUNTIMES):
    s, t = engine.run(
        EXPERIMENTAL='E2',
        DATASET_NAME='1_patel_hurricane_2vs3',
        CLASSIFICATOR='Bayes', # { Bayes, C45, SVM }
        INDIVIDUAL_SIZE=8, # 8 * classes
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

    if TYPE_CALC == 'mean':
        score += s
        time += t

    elif TYPE_CALC == 'max':
        if s > score:
            score = s
            time = t

if TYPE_CALC == 'mean':
    score = score / RUNTIMES
    time = int(time / RUNTIMES)

print('FINAL SCORE: ' + str(score) + ' \t TIME: ' + str(datetime.timedelta(seconds=time)))

