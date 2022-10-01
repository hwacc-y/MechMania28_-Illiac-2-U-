from random import Random
from game.game_state import GameState
import game.character_class
from game.item import Item
import util.utility as util
from game.position import Position
from strategy.strategy import Strategy
import math

center = [Position(4,4),Position(4,5),Position(5,4),Position(5,5)]

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
            
            
        
class Alp_Strategy_Dev(Strategy):
    def strategy_initialize(self, my_player_index: int):
        return game.character_class.CharacterClass.WIZARD

    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        attack_range = 2
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        opponents = []
        #opponents_position = []
        
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])
                #opponents_position.append(player_list[player_index].position)
        
        #center (4,4),(5,4),(4,5)(5,5)
        closest_distance = min(abs(my_position.x - 4) + abs(my_position.y - 4),
                               abs(my_position.x - 4) + abs(my_position.y - 5),
                               abs(my_position.x - 5) + abs(my_position.y - 4),
                               abs(my_position.x - 4) + abs(my_position.y - 5))#|x2 - x1| + |y2 - y1| 
        chosen_opponent = None
        for o in opponents:
            dist = max(abs(my_position.x - o.position.x), abs(my_position.y - o.position.y))
            if( dist < closest_distance and dist < attack_range):
                chosen_opponent = o
                closest_distance = dist
        
        if(chosen_opponent is None): 
            return game_state.player_state_list[my_player_index].position#findClosetCenter(my_position)
        else:
            return game_state.player_state_list[my_player_index].position#o.position

    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return Random().randint(0, 3)

    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.HEAVY_BROADSWORD

    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        player_list = game_state.player_state_list
        my_position = player_list[my_player_index].position
        for c in center:
            if(my_position.x == c.x and my_position.x == c.y):
                return True
        return False