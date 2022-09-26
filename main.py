from cmath import e
from distutils.log import debug
from enum import Enum, auto
from http import client
import json
import logging
from msilib.schema import Error
import sys
from time import sleep
from types import SimpleNamespace

import jsonpickle
from action import buy_action
from action import attack_action
from action import move_action
from action import use_action
from action.attack_action import AttackAction
from action.buy_action import BuyAction
from action.move_action import MoveAction
from action.use_action import UseAction
from game_state import GameState
from networking.client import Client
from networking.comm_state import CommState

from strategy.random_strategy import RandomStrategy

class Phase(Enum):
    USE = auto()
    MOVE = auto()
    ATTACK = auto()
    BUY = auto()

if __name__ == "__main__":

  strategy = RandomStrategy()

  client = Client(29170)

  client.connect()

  logging.basicConfig(    
    format='%(asctime)s %(levelname)-8s %(module)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
  )

  logging.debug("start")


  player_index = -1

  comm_state = CommState.START


  while comm_state != CommState.END:
    logging.debug((comm_state, comm_state==CommState.START))

    if comm_state == CommState.START:
      logging.debug("Waiting for wake...")
      data = client.read()
      if (data.startswith("wake")):
        comm_state = CommState.NUM_ASSIGN
        continue
      continue
    
    if comm_state == CommState.NUM_ASSIGN:
      read = client.read()
      player_index = int(read)
      logging.debug(("Received player index", player_index))
      comm_state = CommState.CLASS_REPORT
      continue

    if comm_state == CommState.CLASS_REPORT:
      character_class = strategy.strategy_initialize()
      client.write(jsonpickle.encode(character_class.name))
      comm_state = CommState.END


  phase = Phase.USE 
  while(True):

    data = client.read()
    
    if (data.startswith("fin")) :
      break

    game_state = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    if phase == Phase.USE :
      use_action = UseAction(player_index, strategy.use_action_decision(game_state, player_index))
      logging.debug(jsonpickle.encode(use_action))
      client.write(jsonpickle.encode(use_action, unpicklable=False))
      phase = Phase.MOVE
      continue
    if phase == Phase.MOVE :
      move_action = MoveAction(player_index, strategy.move_action_decision(game_state, player_index))
      client.write(jsonpickle.encode(move_action, unpicklable=False))
      phase = Phase.ATTACK
      continue
    if phase == Phase.ATTACK :
      attack_action = AttackAction(player_index, strategy.attack_action_decision(game_state, player_index))
      client.write(jsonpickle.encode(attack_action, unpicklable=False))
      phase = Phase.BUY
      continue
    if phase == Phase.BUY :
      buy_action = BuyAction(player_index, strategy.buy_action_decision(game_state, player_index))
      client.write(jsonpickle.encode(buy_action, unpicklable=False))
      phase = Phase.USE
    
  client.disconnect()
