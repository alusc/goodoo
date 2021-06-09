import math

from pygame.math import Vector2

from constants import TILE_SCALE
from displayable import Displayable
from src.projectile import Projectile


class Collectable(Displayable):
    """
    A collectable object is displayable and is
    fixed at one position on the screen.\n
    It can be picked up by an entity when it's colliding with it.\n
    """

    def __init__(self, pos: tuple[int, int], sprite: str, auto_grab: bool = False) -> None:
        super(Collectable, self).__init__(pos, (int(TILE_SCALE * 2 / 3), int(TILE_SCALE * 2 / 3)), sprite=sprite)
        self.__available: bool = True
        self.__origin: Vector2 = Vector2(pos)
        self.__counter: int = 0
        self.__auto_grab: bool = auto_grab

    @property
    def available(self) -> bool:
        return self.__available

    @property
    def auto_grab(self) -> bool:
        return self.__auto_grab

    @available.setter
    def available(self, available: bool) -> None:
        self.__available = available

    def update(self, delta_time: float) -> None:
        self.__counter = (self.__counter + 10) % 360
        self.rect.y = self.__origin.y + (TILE_SCALE / 6) * math.cos(math.radians(self.__counter)) * delta_time
