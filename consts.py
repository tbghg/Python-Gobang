from enum import Enum
from enum import IntEnum

N = 15

class ChessboardState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

class MAP_ENTRY_TYPE(IntEnum):
    MAP_EMPTY = 0,
    MAP_PLAYER_ONE = 1,
    MAP_PLAYER_TWO = 2,
    MAP_NONE = 3,  # 将超出范围设置为3