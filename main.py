import engine

# 0 = 1_patel_hurricane_2vs3
# 1 = 2_patel_hurricane_1vs4
# 2 = 3_patel_hurricane_0vs45
# 3 = 4_patel_animals
# 4 = 5_patel_vehicle



engine.run(
    EXPERIMENTAL='E2',
    DATASET_NAME='1_patel_hurricane_2vs3',
    INDIVIDUAL_SIZE=10,
    POPULATION_SIZE=10,
    ELITE_SIZE=1,
    MUTATION_RATE=0.05,
    GENERATIONS=100
)




