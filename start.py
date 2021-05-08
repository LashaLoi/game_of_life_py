from pygame import event as pg_event, QUIT

from constants import fps, black


def run(grid, screen, clock):
    while True:
        clock.tick(fps)
        screen.fill(black)

        for event in pg_event.get():
            if event.type == QUIT:
                return

        grid.render(screen)
