import itertools
import numpy as np


def _get_genetic_distance(player_1, player_2):
    distance = 0
    if player_1.data.player_id != player_2.data.player_id:
        distance += 1
    if player_1.data.nationality != player_2.data.nationality:
        distance += 1
    if player_1.data.league != player_2.data.league:
        distance += 1
    if player_1.data.club != player_2.data.club:
        distance += 1
    return distance


def get_genetic_distance(individual_1, individual_2):
    player_map_1 = individual_1.player_map
    player_map_2 = individual_2.player_map
    distance = np.mean([_get_genetic_distance(v, player_map_2[k]) for k, v in player_map_1.items()])
    return distance


def speciate(population, treshold=2, max_species=10):
    species = []
    for individual in population:
        matching_species = False
        min_species = None
        min_distance = 0
        for i, s in enumerate(species):
            species_sample = np.random.choice(s)
            distance = get_genetic_distance(individual, species_sample)
            if distance < treshold:
                individual.species = i
                s.append(individual)
                matching_species = True
                break
            if not min_species or distance < min_distance:
                min_species = i
                min_distance = distance
        if not matching_species:
            if len(species) < max_species:
                individual.species = len(species)
                species.append([individual])
            else:
                species[i].append(individual)
    return species


def get_genetic_diversity(species):
    intra_diversity = np.mean([get_genetic_distance(np.random.choice(s1), np.random.choice(s2)) for s1, s2 in itertools.combinations(species, 2)])
    inter_diversity = np.mean([get_genetic_distance(np.random.choice(s), np.random.choice(s)) for s in species])
    return intra_diversity, inter_diversity


def penalise_overpopulation(species, reverse=False):
    for s in species:
        n_individuals = len(s)
        penalty = np.sqrt(n_individuals)
        for i in s:
            if reverse:
                i.fitness *= penalty
            else:
                i.fitness /= penalty
