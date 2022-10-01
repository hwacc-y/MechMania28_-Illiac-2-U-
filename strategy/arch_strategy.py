from random import Random
from game.game_state import GameState
import game.character_class
from game.item import Item
import util.utility as util
from game.position import Position
from strategy.strategy import Strategy
import math

center = [Position(4,4),Position(4,5),Position(5,4),Position(5,5)]

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

def distancetoEnemy(opponents_list: List[PlayerState], my_position: Position)
        temp_dist = abs(position.x - opponent.x) + abs(position.y - opponent.y)

        if( temp_dist < dist and temp_dist < my_attack_range):
            chosen_opponent = o
            dist = temp_dist
    return 

class Arch_Strategy(Strategy):

    #Can you kill anyone in one hit including moves?
    def can_kill(self, game_state: GameState, my_player_index: int) -> int:
        opponents = []
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        attack_range = player_list[my_player_index].stat_set.range
        speed = player_list[my_player_index].stat_set.speed

        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])

        my_position = player_list[my_player_index].position
        chosen_opponent = None
        for o in opponents:
            dist_to_opp = max(abs(my_position.x - o.position.x), abs(my_position.y - o.position.y))
            speed/2
            closest_square = abs(my_position.x - o.position.x) + abs(my_position.y - o.position.y)
            if( dist_to_opp <= attack_range):
                return player_list.index(o)

    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.ARCHER

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        attack_range = 3
        sp_arr = [Position(0,0),Position(9,0),Position(9,9),Position(0,9)]
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        my_health = player_list[my_player_index].health
        my_coin = player_list[my_player_index].gold
        opponents = []
        #opponents_position = []
        
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])
                #opponents_position.append(player_list[player_index].position)
        
        #center (4,4),(5,4),(4,5)(5,5)
        if(my_coin >= 8):
            return sp_arr[my_player_index]

        chosen_opponent = None
        if(chosen_opponent is None): 
            return findClosestCenter(my_position)
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