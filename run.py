# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
    Pipeline for running the simulation.
"""
from competeai.simul import Simulation
from competeai.utils import analysis, aggregate

import os
import yaml
import argparse

# parse the argument
parser = argparse.ArgumentParser()
parser.add_argument('name', type=str)
args = parser.parse_args()

# create a log folder
log_path = f"./logs/{args.name}"

if not os.path.exists(log_path):
    os.makedirs(log_path)
    os.makedirs(f"{log_path}/fig")

config_path = os.path.join('competeai', 'examples', 'group.yaml')
relationship_path = os.path.join('competeai', 'relationship.yaml')

with open(relationship_path, 'r') as f:
    relationship = yaml.safe_load(f)

with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
    config['exp_name'] = args.name
    config['relationship'] = relationship
    Simul = Simulation.from_config(config)
    Simul.run()
    





