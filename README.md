# MechMania28
# ---------------------------- #
# -----------CONTEXT---------- #
# ---------------------------- #

The strategy used currently is alp_strategy. This strat is then piped to build which then produces bot.pyc. 
Start-4-python-bots.bat then runs 4 instances and results are then piped to the web visualizer.

Currently we have built 4 specific strategies. Archer (ar_strategy), Wizard (ma_strategy), Knight (kn_strategy) and Alpha (alp_strategy). a_strategy is to be used a template to fall back on if things go wrong.
# ---------------------------- #
# --------CURRENT WORK-------- #
# ---------------------------- #
Currently we are working on improving the movement of alpha and then testing to see what could be improved as well as continuing development on the other 3 adversary sim strats (Archer, Wizard and Knight). 

# ---------------------------- #
# --------FUTURE WORK--------- #
# ---------------------------- #
We need to make the movement logic work by grabing class data from the player list and thinking about moving into range. 
We most also consider what is the maximum distance we can move towards center as well as if this move would make us go into enemy attack range.
