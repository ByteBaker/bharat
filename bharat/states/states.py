# bharat\states\states.py

import json
from pathlib import Path
from typing import List

from .objects import Date, State

STATES_JSON_FILE = Path(__file__).parent.joinpath('states.json')   # All states data stored here
with open(STATES_JSON_FILE) as states_list:
    list_state_ut_dict = json.load(states_list)          # Is a list[dict]


ALL: List[State] = [None] * len(list_state_ut_dict)      # Should be a list[State]
__all__: List[str] = [None] * len(list_state_ut_dict)    # Module info


for i, state in enumerate(list_state_ut_dict):
    state["statehood_date"] = Date(state["statehood_date"])
    exec(f'{state["abbr"]} = State(**state)')

    ALL[i] = eval(f'{state["abbr"]}')
    __all__[i] = state["abbr"]


STATES: List[State] = [state for state in ALL if not state.is_UT]
UNION_TERRITORIES: List[State] = [state for state in ALL if state.is_UT]

__all__.extend(["STATES", "UNION_TERRITORIES", "ALL"])
