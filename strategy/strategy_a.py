from abc import abstractmethod
from game.game_state import GameState
from game.item import Item
from game.item import Item
from game.position import Position
import game.character_class
import util.utility as util

class Strategy(object):
    """Before the game starts, pick a class for your bot to start with.

    :returns: A game.CharacterClass Enum.
    """
    @abstractmethod
    def strategy_initialize(self, my_player_index: int) -> None:
        return game.character_class.CharacterClass.WIZARD
    """Each turn, decide if you should use the item you're holding. Do not try to use the
    legendary Item.None!

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: If you want to use your item
    """
    @abstractmethod
    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return False
    """Each turn, pick a position on the board that you want to move towards. Be careful not to
    fall out of the board!

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: A game.Position object.
    """
    @abstractmethod
    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        attack_range = 2
        player_list = GameState.player_state_list
        my_position = player_list[my_player_index].position
        opponents = []
        #opponents_position = []
        
        for player_index in range(len(player_list)):
            if(player_index != my_player_index):
                opponents.append(player_list[player_index])
                #opponents_position.append(player_list[player_index].position)
        
        #center (4,4),(5,4),(4,5)(5,5)
        closest_distance = min(util.manhattan_distance(my_position,Position(4,4)),
                               util.manhattan_distance(my_position,Position(4,5)),
                               util.manhattan_distance(my_position,Position(5,4)),
                               util.manhattan_distance(my_position,Position(5,5)))#|x2 - x1| + |y2 - y1| 
        chosen_opponent = None
        for o in opponents:
            dist = util.chebyshev_distance(my_position,o.position)
            if( dist < closest_distance and dist < attack_range):
                chosen_opponent = o
                closest_distance = dist
        
        return Position(4,4)
    """Each turn, pick a player you would like to attack. Feel free to be a pacifist and attack no
    one but yourself.

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: Your target's player index.
    """
    @abstractmethod
    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        while i == my_player_index:
            i = Random().randint(0, 3)
        return i
        """
        player_list = GameState.player_state_list
        my_x_position = player_list[my_player_index].position.x
        my_y_position = player_list[my_player_index].position.y
        if (distance <= attack_range):
            attack 
        """
        
    """Each turn, pick an item you want to buy. Return Item.None if you don't think you can
    afford anything.

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: A game.Item object.

    """
    @abstractmethod
    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE 
        #if ( != ):
            #return "not buy"
