"""Task for creating the state space."""

import numpy as np
import pickle

from young_1993.config import BLD
from young_1993.game.game import define_state_space


def task_define_state_space(
    parameters_dir=BLD / "python" / "game" / "parameters.pkl",
    produces=BLD / "python" / "game" / "states.npy",
):
    """Create the state space."""

    with open(parameters_dir, "rb") as fp:
        parameters = pickle.load(fp)

    num_act = parameters["num_act"]
    num_players = parameters["num_players"]
    m = parameters["m"]

    states = define_state_space(num_act, num_players, m)
    np.save(produces, states)
