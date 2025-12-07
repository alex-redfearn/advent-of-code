class TopographicMap:
    
    _directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    _paths = set()

    def __init__(self, map: dict):
        self._map = map
        self._trailheads = self._trailhead_coordinates(self._map)

    def _trailhead_coordinates(map) -> set:
        trail_heads = set()

        for coordinates in map.keys():
            if map[coordinates] == 0:
                trail_heads.add(coordinates)

        return trail_heads

    def route_count(self) -> int:
        for coordinates in self._trailhead_coordinates:
            self.pathfinder(coordinates)
    
    def pathfinder(self, coordinates):
        value = self._map[coordinates]
        
        if value == 9:
            self._paths.add(coordinates)
            return
            
        for i in range(self._directions.count):
            next_coords = (
                coordinates[0] + self._directions[i][0],
                coordinates[1] + self._directions[i][1]
            )
            
            next_value = self._map[next_coords]
            
            if next_value is None:
                continue
            
            if next_value - value == 1:
                self.pathfinder(next_coords)
            else:
                continue
            
                 

            
            
            
            
        
