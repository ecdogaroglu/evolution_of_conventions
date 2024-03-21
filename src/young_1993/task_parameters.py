"""Task saving the parameters."""

import pytask
import pickle
from young_1993.config import BLD
import numpy as np

parameters = {
    "m": 3,  # memory size - state space grows exponentially in m - long computation time over 4
    "k": 1,  # sample size - possible samples grows exponentially in k - long computation time over 3 - values close to m violate assumptions of the paper
    "epsilon": 0.01,  # experimentation / mistake probability - should be close to zero for asymptotic results
    "num_act": 3,  # number of actions - can be increased more easily
    "num_players": 2,  # number of players - only 2 is supported
}

young_ex_3x3 = [
    [(6, 6), (0, 5), (0, 0)],  # 2x2 example from the original paper
    [(5, 0), (7, 7), (5, 5)],
    [(0, 0), (5, 5), (8, 8)],
]
young_ex_2x2 = [
    [(1, 1), (0, 0)],  # 3x3 example from the original paper
    [(0, 0), (1, 1)],
]

np.random.seed(seed=5324)
np.random.rand(
    parameters["num_act"], parameters["num_act"]
)  # can be used for producing random payoffs

parameters["payoffs"] = young_ex_3x3  # payoffs of the stage game


@pytask.mark.try_first
def task_create_parameters(
    parameters=parameters, produces=BLD / "python" / "game" / "parameters.pkl"
):
    
    for i in ["m", "k", "num_act", "num_players"]:
        if not isinstance(parameters[i],int):
            msg = f"{i} must be int, not {type(parameters[i])}"
            raise TypeError(msg)
        
    for i in ["epsilon"]:
        if not isinstance(parameters[i],(float,int)):
            msg = f"[{i}] must be float, not {type(parameters[i])}"
            raise TypeError(msg)

    for i in ["payoffs"]:
        if not isinstance(parameters[i], (list,np.ndarray)):
            msg = f"{i} must be numpy array, not {type(parameters[i])}"
            raise TypeError(msg)

    for i in ["m", "k", "num_act", "num_players", "epsilon"]:
        if parameters[i] <= 0:
            msg = f"{i} must be positive"
            raise ValueError(msg)
        
    with open(produces, "wb") as fp:
        pickle.dump(parameters, fp)
