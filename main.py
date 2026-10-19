"""Launch the virtual autonomous navigation demo."""

from src.autonav.simulation import Simulation
from src.autonav.visualization import run_app


def main() -> None:
    run_app(Simulation())


if __name__ == "__main__":
    main()
