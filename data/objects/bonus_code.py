from dataclasses import replace
from typing import List

from numpy import cos, ndarray, array
from pygame import Rect, Surface, SRCALPHA, draw, BLEND_RGB_ADD

from data.objects.bonus_data import Bonus
from data.objects.camera_data import Camera
from data.utils.constants import TILE_EDGE, LIGHT_COLOR


def update_bonus(bonus: Bonus, counter: float) -> Bonus:
    """
    Makes the bonus cycle in a movement from top to bottom.

    :param bonus: bonus data
    :param counter: animation counter
    :return: updated bonus data
    """
    rect: Rect = bonus.rect
    rect.y = bonus.origin[1] + cos(counter) * TILE_EDGE / 3
    return replace(bonus, rect=rect)


def destroy_bonus(bonus: Bonus) -> Bonus:
    """
    Destroys the bonus, making it invisible and immune to player collisions.

    :param bonus: bonus data
    :return: updated bonus data
    """
    return replace(bonus, alive=False)


def circle_surface(radius: float) -> Surface:
    surface: Surface = Surface((radius * 2, radius * 2), SRCALPHA)
    draw.circle(surface, LIGHT_COLOR, (radius, radius), radius)
    surface.set_alpha(100)
    return surface


def display_light(screen: Surface, radius: float, pos: ndarray, camera: Camera, counter: float) -> None:
    radius_: List[float] = [radius * (counter % 1), radius * (1 - counter % 1)]
    lights: List[Surface] = [circle_surface(radius) for radius in radius_]

    for i in range(2):
        screen.blit(
            lights[i],
            pos - array((radius_[i], radius_[i]), dtype=int) + camera.offset,
            special_flags=BLEND_RGB_ADD
        )
