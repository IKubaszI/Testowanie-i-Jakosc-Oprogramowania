class LunarVehicle:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.directions = ['N', 'E', 'S', 'W']
        self.dir_index = self.directions.index(direction)

    def turn_left(self):
        self.dir_index = (self.dir_index - 1) % 4

    def turn_right(self):
        self.dir_index = (self.dir_index + 1) % 4

    def move(self):
        direction = self.directions[self.dir_index]
        if direction == 'N':
            self.y += 1
        elif direction == 'S':
            self.y -= 1
        elif direction == 'E':
            self.x += 1
        elif direction == 'W':
            self.x -= 1

    def execute(self, commands):
        for c in commands:
            if c == 'L':
                self.turn_left()
            elif c == 'R':
                self.turn_right()
            elif c == 'M':
                self.move()

    def get_position(self):
        return (self.x, self.y, self.directions[self.dir_index])
