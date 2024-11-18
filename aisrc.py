from fingergame import FingerGame


def set_state(state_list: list):
    state = FingerGame(state_list[9][0], state_list[9][1])
    state.player1.HP = state_list[0]
    state.player1.shield = state_list[1]
    state.player1.left = state_list[2]
    state.player1.right = state_list[3]
    state.player2.HP = state_list[4]
    state.player2.shield = state_list[5]
    state.player2.left = state_list[6]
    state.player2.right = state_list[7]
    state.current_player = state.player1 if state_list[8] else state.player2
    state.waiting_player = state.player2 if state_list[8] else state.player1

    return state


def get_state(state: FingerGame):
    state_list = [0 for _ in range(10)]
    state_list[0] = state.player1.HP
    state_list[1] = state.player1.shield
    state_list[2] = state.player1.left
    state_list[3] = state.player1.right
    state_list[4] = state.player2.HP
    state_list[5] = state.player2.shield
    state_list[6] = state.player2.left
    state_list[7] = state.player2.right
    state_list[8] = 1 if state.current_player == state.player1 else 0
    state_list[9] = state.if_ai

    return state_list


def copy_state(state: FingerGame):
    return set_state(get_state(state))


def copy_list(inlist: list):
    olist = []
    for ele in inlist:
        olist.append(ele)
        return olist


def create_reverse_dict(dictionary: dict):
    reverse_dict = {}
    for key, val in dictionary.items():
        if val not in reverse_dict:
            reverse_dict[val] = [key]
        else:
            reverse_dict[val].append(key)
    return reverse_dict


def print_round(fun):
    def wrapper(self, *args, **kwargs):
        print(get_state(self.state))
        result = fun(self, *args, **kwargs)
        return result
    return wrapper
