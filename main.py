import engine

# 0 = 1_patel_hurricane_2vs3
# 1 = 2_patel_hurricane_1vs4
# 2 = 3_patel_hurricane_0vs45
# 3 = 4_patel_animals
# 4 = 5_patel_vehicle

# engine.run(
#     DATASET_NAME='1_patel_hurricane_2vs3', 
#     INDIVIDUAL_SIZE=100, 
#     POPULATION_SIZE=100, 
#     ELITE_SIZE=2, 
#     MUTATION_RATE=0.01, 
#     GENERATIONS=350
# )

engine.run(
    DATASET_NAME='4_patel_animals', 
    INDIVIDUAL_SIZE=100, 
    POPULATION_SIZE=100, 
    ELITE_SIZE=5, 
    MUTATION_RATE=0.01, 
    GENERATIONS=350
)


