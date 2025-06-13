from typing import Tuple

class LunarRover:
    def __init__(self, start_position: Tuple[int, int] = (0, 0), start_direction: str = 'N'):
        self.position = list(start_position)  # [x, y]
        self.directions = ['N', 'E', 'S', 'W']
        if start_direction not in self.directions:
            raise ValueError("Invalid starting direction.")
        self.direction_index = self.directions.index(start_direction)

    def move_forward(self, steps: int = 1):
        self._move(steps)

    def move_backward(self, steps: int = 1):
        self._move(-steps)

    def rotate_left(self):
        self.direction_index = (self.direction_index - 1) % 4

    def rotate_right(self):
        self.direction_index = (self.direction_index + 1) % 4

    def get_position(self) -> Tuple[int, int]:
        return tuple(self.position)

    def get_direction(self) -> str:
        return self.directions[self.direction_index]

    def _move(self, steps: int):
        direction = self.directions[self.direction_index]
        if direction == 'N':
            self.position[1] += steps
        elif direction == 'S':
            self.position[1] -= steps
        elif direction == 'E':
            self.position[0] += steps
        elif direction == 'W':
            self.position[0] -= steps
