from ..nsga2.stopper import make_stopper


def test_invalid_stopper_id():
    stopper_id = "InvalidStopper"
    error_thrown = False
    try:
        stopper = make_stopper(stopper_id)
    except ValueError:
        error_thrown = True
    assert error_thrown


def test_valid_stopper_id():
    stopper_id = "MaxGenerationStopper"
    error_thrown = False
    try:
        stopper = make_stopper(stopper_id)
    except ValueError:
        error_thrown = True
    assert not error_thrown


def test_invalid_stopper_kwargs():
    stopper_id = "MaxGenerationStopper"
    stopper_kwargs = {"invalid_param": 0}
    error_thrown = False
    try:
        stopper = make_stopper(stopper_id, stopper_kwargs)
    except TypeError:
        error_thrown = True
    assert error_thrown


def test_invalid_stopper_kwargs():
    stopper_id = "MaxGenerationStopper"
    stopper_kwargs = {"max_generations": 10}
    error_thrown = False
    try:
        stopper = make_stopper(stopper_id, stopper_kwargs)
    except TypeError:
        error_thrown = True
    assert not error_thrown


def test_not_stop():
    stopper_id = "MaxGenerationStopper"
    stopper_kwargs = {"max_generations": 100}
    stopper = make_stopper(stopper_id, stopper_kwargs)
    state = {"current_generation": 99}
    assert not stopper.stop(state)


def test_not_stop():
    stopper_id = "MaxGenerationStopper"
    stopper_kwargs = {"max_generations": 100}
    stopper = make_stopper(stopper_id, stopper_kwargs)
    state = {"current_generation": 101}
    assert stopper.stop(state)
