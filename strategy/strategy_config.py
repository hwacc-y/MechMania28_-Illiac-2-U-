from strategy.starter_strategy import StarterStrategy
from strategy.strategy import Strategy
from strategy.alp_strategy import Alp_Strategy
from strategy.kn_strategy import Kngt_Strategy
from strategy.alp_strategy_dev import Alp_Strategy_Dev
#from strategy.ar_strategy import Arch_Strategy
#from strategy.ma_strategy import Wzrd_Strategy
"""Return the strategy that your bot should use.

:param playerIndex: A player index that can be used if necessary.

:returns: A Strategy object.
"""
def get_strategy(player_index: int) -> Strategy:  
  x = player_index
  if (x == 0):
    return Alp_Strategy_Dev() 
  if (x == 1):
    return Alp_Strategy()
  if (x == 2):
    return Kngt_Strategy()
  if (x == 3):
    return Alp_Strategy()