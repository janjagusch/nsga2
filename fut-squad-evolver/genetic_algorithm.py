import copy
import numpy as np
from formation_base import get_positions, players


COMPATIBLE_POSITIONS = {k: v.get_compatible_positions(2) for k, v in get_positions().items()}
COMPATIBLE_PLAYERS = {}
for k, v in COMPATIBLE_POSITIONS.items():
    condition = np.vectorize(lambda x: x.position in v)(players)
    COMPATIBLE_PLAYERS[k] = np.extract(condition, players)

    
EQUAL_PLAYERS = {}
for player in players:
    k = (player.data.player_extended_name, player.data.date_of_birth) 
    if k not in EQUAL_PLAYERS.keys():
        EQUAL_PLAYERS[k] = []
    EQUAL_PLAYERS[k].append(player)

    
def get_equal_players(player):
    k = (player.data.player_extended_name, player.data.date_of_birth)
    return EQUAL_PLAYERS[k]


class Individual:
    
    def __init__(self, player_map, formation, fitness=None):
        """
        Creates Individual instance.
        Args:
            player_map: dictionary, where key is slot_id and value is Player instance.
            fitness: float value.
        Returns:
            instance of class Individual.
        """
        self.player_map = player_map
        self.formation = formation
        self.fitness = fitness
    
    def fill(self):
        """Fills formation with player_map."""
        for k, v in self.formation.slots.items():
            v.player = self.player_map[k]
        return self.formation        
        
    def evaluate(self, loss):
        """Evaluates formation based on player_map."""
        self.fill()
        self.fitness = loss(self.formation)
        return self.fitness
    
    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __le__(self, other):
        return self.fitness <= other.fitness
    
    def __eq__(self, other):
        return self.fitness == other.fitness
    
    def __ge__(self, other):
        return self.fitness >= other.fitness
    
    def __gt__(self, other):
        return self.fitness > other.fitness
    
    def __repr__(self):
        return "{}(player_map={}, fitness={})".format(self.__class__.__name__, self.player_map, self.fitness)

    
def initialise_individual(formation):
    """Creates individual by creating random player_map based on formation."""
    player_map = {}
    for k, v in formation.slots.items():
        player = None
        while not player or player in player_map.values():
            player = np.random.choice(COMPATIBLE_PLAYERS[v.position.id])
        player_map[k] = player  
    individual = Individual(player_map, formation)
    return individual


def select_individuals(population, tournament_size=5):
    """Selects fittest individuals from population using tournament selection."""
    selected_individuals = []
    for i in range(len(population)):
        tournament = np.random.choice(population, size=tournament_size)
        winner = copy.deepcopy(tournament[np.argmax(tournament)])
        selected_individuals.append(winner)
    return selected_individuals


def mutate_individual(individual, replace_prop=0.75, swap_prop=0.2, switch_prop=0.05):
    """Mutates individual with three different mutation strategies."""
    formation = individual.formation
    # Replace mutation.
    if np.random.uniform() < replace_prop:
        random_slots = np.random.choice(list(formation.slots.keys()), 1)
        for k in random_slots:
            player = None
            while not player or player in individual.player_map.values():
                player = np.random.choice(COMPATIBLE_PLAYERS[formation.slots[k].position.id])
            individual.player_map[k] = player
    # Swap mutation.    
    if np.random.uniform() < swap_prop:
        random_slot_1 = formation.slots[np.random.choice(list(individual.player_map.keys()))]
        random_slot_2 = np.random.choice(random_slot_1.get_linked_slots())
        individual.player_map[random_slot_1.slot_id], individual.player_map[random_slot_2.slot_id] = individual.player_map[random_slot_2.slot_id], individual.player_map[random_slot_1.slot_id]
    # Switch mutation.
    if np.random.uniform() < switch_prop:
        random_slot = formation.slots[np.random.choice(list(individual.player_map.keys()))]
        individual.player_map[random_slot.slot_id] = np.random.choice(get_equal_players(individual.player_map[random_slot.slot_id]))

        
def crossover_individuals(individual_1, individual_2, formation):
    """Applies crossover between two different individuals."""
    formation = individual_1.formation
    random_slot = formation.slots[np.random.choice(list(individual_1.player_map.keys()))]
    random_slots = [random_slot] + random_slot.get_linked_slots()
    random_slots = [s.slot_id for s in random_slots]
    for k in random_slots:
        player_1 = individual_1.player_map[k]
        player_2 = individual_2.player_map[k]
        
        if player_2 in individual_1.player_map.values() and player_1 != player_2:
            player = None
            while not player or player in individual_1.player_map.values():
                player = np.random.choice(COMPATIBLE_PLAYERS[formation.slots[k].position.id])
            individual_1.player_map[k] = player
        else:
            individual_1.player_map[k] = player_2
        
        if player_1 in individual_2.player_map.values() and player_1 != player_2:
            player = None
            while not player or player in individual_2.player_map.values():
                player = np.random.choice(COMPATIBLE_PLAYERS[formation.slots[k].position.id])
            individual_2.player_map[k] = player
        else:
            individual_2.player_map[k] = player_1