from random import Random
from game.game_state import GameState
import game.character_class
from game.item import Item
import util.utility as util
from game.position import Position
from strategy.strategy import Strategy
import math
import config
from typing import List
 
center = [Position(4,4),Position(4,5),Position(5,4),Position(5,5)]
 
def in_bounds(p: Position) -> bool:
    #  Assume board runs from 0 to BOARD_SIZE - 1
    return ((p.x >= 0) and (p.x < config.BOARD_SIZE) and (p.y >= 0) and (p.y < config.BOARD_SIZE))

def manhattan_distance(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
 
def chebyshev_distance(p1: Position, p2: Position) -> int:
    return max(abs(p1.x - p2.x), abs(p1.y - p2.y))
 
def findClosestCenter(position: Position):
    closest_dist = None
    target_index = None
    for i in range(len(center)):
        if closest_dist is None:
            closest_dist = abs(position.x - center[i].x) + abs(position.y - center[i].y)
            target_index = i
        elif((abs(position.x - center[i].x) + abs(position.y - center[i].y)) < closest_dist):
            closest_dist = abs(position.x - center[i].x) + abs(position.y - center[i].y)
            target_index = i
    return center[i]
 
def findClosestDistance(position: Position):
 
    closest_distance = min(abs(position.x - 4) + abs(position.y - 4),
                               abs(position.x - 4) + abs(position.y - 5),
                               abs(position.x - 5) + abs(position.y - 4),
                               abs(position.x - 4) + abs(position.y - 5))#|x2 - x1| + |y2 - y1|
    return closest_distance
 
def get_reachable_tiles(my_position: Position, my_speed: int) -> List[tuple]:
    reachable_list = []
    for x in range(-my_speed, my_speed+1):
        for y in range(-my_speed, my_speed+1):
            if chebyshev_distance(my_position, Position(x,y)) and in_bounds(Position(x,y)):
                reachable_list.append((my_position.x + x, my_position.y + y))
               
    return reachable_list
 
class Arch_Strategy(Strategy):
 
    # #Can you kill anyone in one hit including moves?
    # def can_kill(self, game_state: GameState, my_player_index: int) -> int:
    #     opponents = []
    #     player_list = game_state.player_state_list
    #     my_position = player_list[my_player_index].position
    #     attack_range = player_list[my_player_index].stat_set.range
    #     speed = player_list[my_player_index].stat_set.speed
 
    #     for player_index in range(len(player_list)):
    #         if(player_index != my_player_index):
    #             opponents.append(player_list[player_index])
 
    #     my_position = player_list[my_player_index].position
    #     chosen_opponent = None
    #     for o in opponents:
    #         dist_to_opp = max(abs(my_position.x - o.position.x), abs(my_position.y - o.position.y))
    #         speed/2
    #         closest_square = abs(my_position.x - o.position.x) + abs(my_position.y - o.position.y)
    #         if( dist_to_opp <= attack_range):
    #             return player_list.index(o)
 
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.ARCHER
 
    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        attack_range = 3
        sp_arr = [Position(0,0),Position(9,0),Position(9,9),Position(0,9)]
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        my_health = player_list[my_player_index].health
        my_coin = player_list[my_player_index].gold
        my_speed = player_list[my_player_index].stat_set.speed
        opponents = []
        #opponents_position = []
       
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])
                #opponents_position.append(player_list[player_index].position)
       
        possible_moves = get_reachable_tiles(my_position, my_speed)
        biggest_enemy_distance = 0
        position = ()
 
        for temp in possible_moves:
            total_enemy_distance = 0
            for o in opponents:
                total_enemy_distance  += manhattan_distance(Position(temp[0], temp[1]), o.position)

            if total_enemy_distance > biggest_enemy_distance and findClosestDistance(Position(temp[0], temp[1])) <= my_speed:
                biggest_enemy_distance = total_enemy_distance
                position = Position(temp[0], temp[1])
            
        #center (4,4),(5,4),(4,5)(5,5)
        if(my_coin >= 8):
            return sp_arr[my_player_index]
 
        chosen_opponent = None
        if(chosen_opponent is None):
            if findClosestDistance <= my_speed:
                return findClosestCenter(my_position)
            else:
                return position
        else:
            return chosen_opponent.position
 
 
    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return 0
 
    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        player_list = game_state.player_state_list
        my_coin = player_list[my_player_index].gold
        if(my_coin >= 8):
            return Item.SPEED_POTION
        else:
            return Item.NONE
 
    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        if findClosestDistance(my_position) <= 6 and findClosestDistance(my_position) > 4:
            return True
        else:
            return False