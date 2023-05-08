from enum import Enum


class Wait(Enum):
    """
    Enum class to handle default wait timers with each
    value increasing by a factor of ~3.
    """
    VERY_SHORT: int = 1
    SHORT: int = 3
    MEDIUM: int = 10
    LONG: int = 30
    VERY_LONG: int = 90
