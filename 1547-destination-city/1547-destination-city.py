class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set_start = set()
        set_end = set()
        for path in paths:
            set_start.add(path[0])
            set_end.add(path[1])

        for destination in set_end:
            if destination not in set_start:
                return destination
        
        return []
        