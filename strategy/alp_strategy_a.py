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

def manhattan_distance(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def chebyshev_distance(p1: Position, p2: Position) -> int:
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y))

def findClosetCenter(position: Position):
    closet_dist = None
    target_index = None

    for i in range(len(center)):
        if closet_dist is None:
            closet_dist = abs(position.x - center[i].x) + abs(position.y - center[i].y)
            target_index = i
        elif((abs(position.x - center[i].x) + abs(position.y - center[i].y)) < closet_dist):
            closet_dist = abs(position.x - center[i].x) + abs(position.y - center[i].y)
            target_index = i

    return center[i]

def get_closest_opponent_in_attackRange(opponents_list: List[PlayerState], my_position: Position, my_attack_range: int) -> PlayerState:
    chosen_opponent = None
    dist = 100
    for o in opponents_list:
        temp_dist = chebyshev_distance(my_position, o.position)
        if( temp_dist < dist and temp_dist < my_attack_range):
            chosen_opponent = o
            dist = temp_dist
    return chosen_opponent
        
class Alp_Strategy_A(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.KNIGHT

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        attack_range = 2
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        player = player_list[my_player_index]
        opponents = []
        sp_arr = [Position(0,0), Position(9,0), Position(9,9), Position(0,9)]
        
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])

        closest_distance = min(abs(my_position.x - 4) + abs(my_position.y - 4),
                               abs(my_position.x - 4) + abs(my_position.y - 5),
                               abs(my_position.x - 5) + abs(my_position.y - 4),
                               abs(my_position.x - 4) + abs(my_position.y - 5)) # |x2 - x1| + |y2 - y1| 
        chosen_opponent = None

        for o in opponents:
            dist = max(abs(my_position.x - o.position.x), abs(my_position.y - o.position.y))
            
            if( dist < closest_distance and dist < attack_range):
                chosen_opponent = o
                closest_distance = dist
        
        # if player.health <= round(player.stat_set.max_health/3):
        #     return sp_arr[my_player_index]

        if player.item == Item.NONE and player.gold >= 8:
            return player.position
        elif chosen_opponent is None: 
            return findClosetCenter(my_position)
        else:
            return o.position
            # return findClosetCenter(my_position)

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        # return Random().randint(0, 3)

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

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:  
        player_list = game_state.player_state_list
        my_coin = player_list[my_player_index].gold

        if my_coin >= 8:
            return Item.HUNTER_SCOPE
        return Item.NONE

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return True