#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import torch


# Config that serves all environment
GLOBAL_CONFIG = {
    "MODEL_PATH": "../model/model.pt",
    "SCALAR_PATH": "../model/scaler.joblib",
    "USE_CUDE_IF_AVAILABLE": True,
    "ROUND_DIGIT": 6
}

# Environment specific config, or overwrite of GLOBAL_CONFIG
ENV_CONFIG = {
    "development": {
        "DEBUG": True
    },

    "staging": {
        "DEBUG": True
    },

    "production": {
        "DEBUG": False,
        "ROUND_DIGIT": 3
    }
}


def get_config() -> dict:
    """
    Get config based on running environment

    :return: dict of config
    """

    # Determine running environment
    ENV = os.environ['PYTHON_ENV'] if 'PYTHON_ENV' in os.environ else 'development'
    ENV = ENV or 'development'

    # raise error if environment is not expected
    if ENV not in ENV_CONFIG:
        raise EnvironmentError(f'Config for envirnoment {ENV} not found')

    config = GLOBAL_CONFIG.copy()
    config.update(ENV_CONFIG[ENV])

    config['ENV'] = ENV
    config['DEVICE'] = 'cuda' if torch.cuda.is_available() and config['USE_CUDE_IF_AVAILABLE'] else 'cpu'

    return config

# load config for import
CONFIG = get_config()

if __name__ == '__main__':
    # for debugging
    import json
    print(json.dumps(CONFIG, indent=4))
