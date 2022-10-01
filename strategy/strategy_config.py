from strategy.starter_strategy import StarterStrategy
from strategy.strategy import Strategy
from strategy.alp_strategy import Alp_Strategy
"""Return the strategy that your bot should use.

:param playerIndex: A player index that can be used if necessary.

:returns: A Strategy object.
"""
def get_strategy(player_index: int) -> Strategy:  
  
  return Alp_Strategy()