from copy import deepcopy
from direction import Direction
from position import Position

class Game:

    EMPTY_SPACE = "."
    OBSTACLE = "#"

    def __init__(self, map: dict[tuple, str]):
        self.map = map

    def start(self):
        self.play()
        
    def loop_count(self, start_position: Position) -> int:
        loop_count = 0

        for coordinates in self.map.keys():
            if self.map[coordinates] != self.EMPTY_SPACE:
                continue

            self.map[coordinates] = self.OBSTACLE  # Place obstacle
            
            final_position = self.play(start_position)
            
            self.map[coordinates] = self.EMPTY_SPACE  # revert

            if final_position is not None:
                loop_count += 1

        return loop_count
    
    def play(self, position):
        foot_steps = set()

        while True:

            # Get next pos
            next_coordinates = (position.coordinates[0] + position.direction.row, position.coordinates[1] + position.direction.col)
            next_position = Position(next_coordinates, position.direction)
            next_value = self.map.get((next_position.coordinates[0], next_position.coordinates[1]))
            
            if (next_position.coordinates, next_position.direction) in foot_steps:
                return position
                
            if self.move_available(next_value):
                position = next_position
                foot_steps.add((position.coordinates, position.direction))
                continue

            if self.collision(next_value):
                position = Position(position.coordinates, Direction.turn_right(position.direction))
                continue
            
            if next_value is None:
                return None

    def move_available(self, value):
        return value == self.EMPTY_SPACE or value == "^"
    
    def collision(self, value):
        return value == self.OBSTACLE
        
    def loop_created(self, start_position, current_position):
        return start_position == current_position