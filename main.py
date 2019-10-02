import engine

# 0 = 1_patel_hurricane_2vs3
# 1 = 2_patel_hurricane_1vs4
# 2 = 3_patel_hurricane_0vs45
# 3 = 4_patel_animals
# 4 = 5_patel_vehicle

# 5 = Foursquare

engine.run(
    DATASET_NAME='Foursquare', 
    INDIVIDUAL_SIZE=35, 
    POPULATION_SIZE=20, 
    ELITE_SIZE=2, 
    MUTATION_RATE=0.2, 
    GENERATIONS=350
)


