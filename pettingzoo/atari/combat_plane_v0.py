from .base_atari_env import BaseAtariEnv, base_env_wrapper_fn

avaliable_versions = {
    "bi-plane": 15,
    "jet": 21,
}

def raw_env(game_version="bi-plane", guided_missile=True, **kwargs):
    assert game_version in avaliable_versions, "game_version must be either 'jet' or 'bi-plane'"
    mode = avaliable_versions[game_version] + (0 if guided_missile else 1)

    return BaseAtariEnv(game="combat", num_players=2, mode_num=mode, **kwargs)


env = base_env_wrapper_fn(raw_env)
