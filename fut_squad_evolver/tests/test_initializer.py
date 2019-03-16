from ..nsga2.initializer import make_initializer
from ..utils.data_loader import FORMATIONS, PLAYERS, COMPATIBLE_PLAYERS


def test_invalid_initializer_id():
    initializer_id = "InvalidInitializer"
    error_thrown = False
    try:
        initializer = make_initializer(initializer_id,
                                       initializer_kwargs={"formation": FORMATIONS,
                                       "players": PLAYERS})
    except ValueError:
        error_thrown = True
    assert error_thrown
