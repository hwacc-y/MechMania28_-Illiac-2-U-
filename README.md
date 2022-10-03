# MechMania28
# ---------------------------- #
# -----------CONTEXT---------- #
# ---------------------------- #

This set of code was developed from the python starter pack cloned from the MechMania28 repo (https://github.com/MechMania-28/Python-Starterpack). The code within this repo were written by @rayko9277 (Ray Ko), @ZYCC6002 (Chris Chan), @SidharthAnand04 (Sidharth Anand) and hwacc-y (Nicholas Yeung). Our team, Illiac 2 and U, placed 9th using the ranger.py strategy file. Other strategy files such as kn_strategy and wiz_stragety were also quite effective for a while until balacing updates to the game reduced their effectiveness. 

# ------------------------------------- #
# -----------Running the code---------- #
# --------------------------------------#

Code Req:
Java >= 11  
Node.js
Python >= 3.8
----------------------
pip install jsonpickle
----------------------
First run the Engine.jar file from (https://github.com/MechMania-28/Engine)
Next run the build.py file 
Then run the start-4-python-bots.bat/.sh file
After that the engineer should output a .json file in a folder called gamelogs, which is located in the same directory as Engine.jar.
Run the resulting JSON file in the visualizer (https://github.com/MechMania-28/Visualizer) to render the results.
---------------------------------------------------------------------------
Tips:
I configured the strategy_config.py file so that it can test out multiple strategies against each other during tests. If you want the engine to run the game with 4 bots running the same strategy just make test = false and return the desired strat function in the return statement under else.
---------------------------------------------------------------------------
# ---------------------------- #
# --------CURRENT WORK-------- #
# ---------------------------- #
Currently the hackathon is over but maybe in the furture, I'll come back to tinker with this repo.

# ---------------------------- #
# --------FUTURE WORK--------- #
# ---------------------------- #
Maybe try and optimize the knight or wizard class using other ML methods such as reinforcement learning since there is no longer a time constraint.