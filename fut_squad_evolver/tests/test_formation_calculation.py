from ..nsga2.initializer import Initializer
from ..formation_calculations.calculate import calculate_metrics
from ..utils import data_loader


def test_calculate_metrics():
    formation = data_loader.FORMATIONS["442"]
    initializer = Initializer(
        formation,
        data_loader.PLAYERS,
        data_loader.COMPATIBLE_PLAYERS
    )
    squad = initializer.initialize()
    metrics = calculate_metrics(squad, formation)
    assert isinstance(metrics, dict)
    assert all(metric in metrics.keys() for metric in ["price", "rating", "chemistry"])
    assert all(metric in ["price", "rating", "chemistry"] for metric in metrics.keys())
    assert metrics["price"] > 0
    assert metrics["rating"] >= 0
    assert metrics["rating"] <= 100
    assert metrics["chemistry"] >= 0
    assert metrics["chemistry"] <= 100
