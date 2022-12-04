import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color, position):
        super().__init__()
        self._cycle_color = color
        self._segments = []
        self._head = Actor()
        self._head.set_color(color)
        self._head.set_text('@')
        self._head.set_position(position)
        self._segments.append(self._head)

    def get_segments(self):
        return self._segments

    def move_next(self):
       self._segments[0].move_next()

       self._tail = Actor()
       self._tail.set_color(self._cycle_color)
       self._tail.set_text('#')
       self._segments.append(self._tail)
       self._tail.set_position(self._head.get_position())

    def get_head(self):
        return self._segments[0]

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
   