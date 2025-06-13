from collections import Counter
from typing import List, Optional

class Lottery:

    def __init__(self, numbers: Optional[List[int]]):
        self.numbers = numbers or []

    def find_repeated_sets(self, target_count: int) -> List[int]:

        if not isinstance(target_count, int) or target_count < 1:
            return []

        frequency = Counter(self.numbers)
        return [num for num, count in frequency.items() if count == target_count]
