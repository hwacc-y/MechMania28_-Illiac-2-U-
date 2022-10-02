from random import Random
from typing import List
import random
from game.game_state import GameState
import game.character_class
from game.item import Item  
import util.utility as util
from game.position import Position
from strategy.strategy import Strategy
from game.player_state import PlayerState
import math

center = [Position(4,4),Position(4,5),Position(5,4),Position(5,5)]
sp_arr = [Position(0,0), Position(9,0), Position(9,9),Position(0,9)]

def manhattan_distance(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
 
def chebyshev_distance(p1: Position, p2: Position) -> int:
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y))

def opponent_search(opponents, player):
    for o in opponents: 
        distance = chebyshev_distance(o.position, player.position)
        if distance <= o.stat_set.range: 
            return True
    return False

def get_closest_opponent_in_attackRange(opponents_list: List[PlayerState], my_position: Position, my_attack_range: int) -> PlayerState:
    chosen_opponent = None
    dist = 100
    for o in opponents_list:
        temp_dist = chebyshev_distance(my_position, o.position)
        if( temp_dist < dist and temp_dist < my_attack_range):
            chosen_opponent = o
            dist = temp_dist
    return chosen_opponent

def find_closest_center(position: Position) -> Position:
    target_index = 0
    closest_dist = manhattan_distance(position,center[0])
    for i in range(len(center)):
        if(manhattan_distance(position,center[i]) < closest_dist):
            closest_dist = manhattan_distance(position,center[i])
            target_index = i
    return center[target_index]

def is_center(my_position: Position):
    for p in center:
        if(my_position.x == p.x and my_position.y == p.y):
            return True
    return False

class BestieStrat(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.WIZARD

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        #if can oneshot someone, ONESHOT THEM
        #if  cannot kill anyone, move to center

        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        my_coin = player_list[my_player_index].gold
        my_health = player_list[my_player_index].health
        my_range = player_list[my_player_index].stat_set.range
        my_item = player_list[my_player_index].item

        go_back = is_center(my_position)*random.randint(0, 1)

        if my_coin >= 8 and my_health <= 3 and not go_back:
            return sp_arr[my_player_index]
        
        return find_closest_center(my_position)
       
    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        opponents = []
        player_list = game_state.player_state_list
        player = game_state.player_state_list[my_player_index]
 
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])
       
        opponent = get_closest_opponent_in_attackRange(opponents, player_list[my_player_index].position, player_list[my_player_index].stat_set.range)
 
        if opponent is not None:
            distance = chebyshev_distance(opponent.position, player.position)
 
            if distance <= player.stat_set.range:
                return player_list.index(opponent)
 
        return my_player_index

        #Attack

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        player_list = game_state.player_state_list
        my_coin = player_list[my_player_index].gold
        if(my_coin >= 8):
            return Item.SHIELD
        else:
            return Item.NONE
            
    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        opponents = []
        player_list = game_state.player_state_list
        player = game_state.player_state_list[my_player_index]
 
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])

        should_use = opponent_search(opponents, player)
        return should_use

