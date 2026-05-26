# Requires: pip install windows-curses  (Windows only)
import curses
import random

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(120)

    h, w = stdscr.getmaxyx()

    snake = [(h // 2, w // 4 + i) for i in range(4, -1, -1)]
    direction = curses.KEY_RIGHT

    def place_food():
        while True:
            pos = (random.randint(1, h - 2), random.randint(1, w - 2))
            if pos not in snake:
                return pos

    food = place_food()
    score = 0

    while True:
        stdscr.erase()
        stdscr.border()
        stdscr.addstr(0, 2, f" Score: {score} ")
        stdscr.addstr(0, w - 18, " Q to quit ")

        stdscr.addch(food[0], food[1], '@')

        for i, seg in enumerate(snake):
            stdscr.addch(seg[0], seg[1], 'O' if i == 0 else 'o')

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
            opposite = {
                curses.KEY_UP: curses.KEY_DOWN,
                curses.KEY_DOWN: curses.KEY_UP,
                curses.KEY_LEFT: curses.KEY_RIGHT,
                curses.KEY_RIGHT: curses.KEY_LEFT,
            }
            if key != opposite[direction]:
                direction = key

        r, c = snake[0]
        if direction == curses.KEY_UP:    r -= 1
        elif direction == curses.KEY_DOWN:  r += 1
        elif direction == curses.KEY_LEFT:  c -= 1
        elif direction == curses.KEY_RIGHT: c += 1

        new_head = (r, c)

        if r in (0, h - 1) or c in (0, w - 1) or new_head in snake:
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = place_food()
        else:
            snake.pop()

    stdscr.nodelay(False)
    stdscr.erase()
    stdscr.border()
    msg = f"Game Over! Score: {score}  (press any key)"
    stdscr.addstr(h // 2, (w - len(msg)) // 2, msg)
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
