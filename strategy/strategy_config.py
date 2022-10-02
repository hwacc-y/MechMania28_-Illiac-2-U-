from strategy.starter_strategy import StarterStrategy
from strategy.strategy import Strategy
from strategy.alp_strategy import Alp_Strategy
from strategy.kn_strategy import Kngt_Strategy
from strategy.alp_strategy_dev import Alp_Strategy_Dev
from strategy.bestie import BestieStrat
from strategy.ranger import RangerStrat
from strategy.arch_strategy import Arch_Strategy
from strategy.alp_strategy_a import Alp_Strategy_A
#from strategy.ma_strategy import Wzrd_Strategy
"""Return the strategy that your bot should use.

:param playerIndex: A player index that can be used if necessary.

:returns: A Strategy object.
"""
def get_strategy(player_index: int) -> Strategy:  
  x = player_index
  test = False
  if (x == 0) & (test):
    return Kngt_Strategy() 
  if (x == 1) & (test):
    return BestieStrat() 
  if (x == 2) & (test):
    return Alp_Strategy_A()
  if (x == 3) & (test):
    return RangerStrat()
  else:
    return RangerStrat()

