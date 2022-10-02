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

def same_pos(p1, p2):
    if p1.x - p2.x == 0 and p1.y - p2.y == 0:
        return True
    return False

def center_opponents(opponents):
    list = []
    for i in center:
        for o in opponents:
            if o.position.x == i.x and o.position.y == i.y:
                list.append(o)
    return list

def in_bounds(p: Position) -> bool:
    #  Assume board runs from 0 to BOARD_SIZE - 1
    return ((p.x >= 0) and (p.x < config.BOARD_SIZE) and (p.y >= 0) and (p.y < config.BOARD_SIZE))

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
    dist = chebyshev_distance(my_position, opponents_list[0].position)

    for o in opponents_list:
        temp_dist = chebyshev_distance(my_position, o.position)
        if( temp_dist < dist and temp_dist <= my_attack_range):
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

def best_attack_space(opponents_list:List[PlayerState], my_position) -> Position:
    center_opponents_list = center_opponents(opponents_list)
    if center_opponents_list:
        opponent = center_opponents_list[0]
        move = random.randint(0, 1)
        m1 = manhattan_distance(my_position, Position(opponent.position.x + move, opponent.position.y - move))
        m2 = manhattan_distance(my_position, Position(opponent.position.x - move, opponent.position.y - move))
        m3 = manhattan_distance(my_position, Position(opponent.position.x + move, opponent.position.y + move))
        m4 = manhattan_distance(my_position, Position(opponent.position.x - move, opponent.position.y + move))
        if (m1 < m2 and m1 < m3 and m1 < m4):
            return Position(opponent.position.x + move, opponent.position.y - move)
        elif m2 < m3 and m2 < m4:
            return Position(opponent.position.x - move, opponent.position.y - move)
        elif m3 < m4:
            return Position(opponent.position.x + move, opponent.position.y + move)
        else:
            return Position(opponent.position.x - move, opponent.position.y + move)

        # test_pos = Position(opponent.position.x + 2, opponent.position.y + 2)
        # if in_bounds(test_pos):
        #     return test_pos
        # elif in_bounds(Position(opponent.position.x + 2, opponent.position.y - 2)):
        #     return Position(opponent.position.x + 2, opponent.position.y - 2)
        # elif in_bounds(Position(opponent.position.x - 2, opponent.position.y + 2)):
        #     return Position(opponent.position.x - 2, opponent.position.y + 2)
        # else:
        #     test_pos = Position(opponent.position.x - 2, opponent.position.y - 2)
        #     return test_pos 

        # get_closest_opponent_in_attackRange(center_opponents_list, my_position: Position, my_attack_range: int)
        # for center_opponent in center_opponents_list:
        #     center_opponent_position = center_opponent.position
        #     for

class RangerStrat(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.ARCHER

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        #if can oneshot someone, ONESHOT THEM
        #if  cannot kill anyone, move to center

        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        my_coin = player_list[my_player_index].gold
        my_health = player_list[my_player_index].health
        my_range = player_list[my_player_index].stat_set.range
        my_item = player_list[my_player_index].item
        all_opponents = player_list[:my_player_index] + player_list[my_player_index+1:]

        go_back = is_center(my_position)*random.randint(1, 2)

        is_spawn = False 
        
        for pos in sp_arr: 
            if same_pos(my_position, pos):
                is_spawn = True
                break

        if (my_coin >= 8 and my_health <= 4 and not go_back) or (is_spawn and my_coin >= 8):
            return sp_arr[my_player_index]
        
        center_opponent_list = center_opponents(all_opponents)
        if len(center_opponent_list) == 0:
            return find_closest_center(my_position)
        elif not is_center(my_position):
            return best_attack_space(center_opponent_list, my_position)
        else:
            return my_position
            

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        opponents = []
        player_list = game_state.player_state_list
        player = game_state.player_state_list[my_player_index]
        my_position = player_list[my_player_index].position
        
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])
                if chebyshev_distance(my_position, player_list[player_index].position) <= player_list[my_player_index].stat_set.range:
                    return player_index
            
        return my_player_index
        # opponent = get_closest_opponent_in_attackRange(opponents, player_list[my_player_index].position, player_list[my_player_index].stat_set.range)
 
        # if opponent is not None:
        #     return player_list.index(opponent)
        # return my_player_index

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

