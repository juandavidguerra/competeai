# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from .base import Scene
from .restaurant_design import RestaurantDesign
from .dine import Dine
from .group_dine import GroupDine
from ..config import SceneConfig

ALL_SCENES = [
    RestaurantDesign,
    Dine,
    GroupDine,
]

SCENE_REGISTRY = {scene.type_name: scene for scene in ALL_SCENES}


# load a scene from a config dictionary
def load_scene(config: SceneConfig):
    try:
        scene_cls = SCENE_REGISTRY[config["scene_type"]]
    except KeyError:
        raise ValueError(f"Unknown scene type: {config['scene_type']}")

    scene = scene_cls.from_config(config)
    return scene

