from pygame import quit

from config import get_config
from start import run

if __name__ == "__main__":
    (grid, screen, clock) = get_config()

    run(grid, screen, clock)
    quit()
