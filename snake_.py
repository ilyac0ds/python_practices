import tkinter as tk
import random


# =========================
# SETTINGS
# =========================

WIDTH = 600
HEIGHT = 600
CELL = 30

COLS = WIDTH // CELL
ROWS = HEIGHT // CELL

SPEED = 100


# =========================
# GAME
# =========================

class SnakeGame:

    def __init__(self, root):

        self.root = root
        self.root.title("NEON SNAKE")
        self.root.resizable(False, False)
        self.root.configure(bg="#0b0f14")

        self.running = False

        # Header
        self.header = tk.Frame(
            root,
            bg="#0b0f14",
            height=70
        )

        self.header.pack(fill="x")

        self.title = tk.Label(
            self.header,
            text="NEON SNAKE",
            font=("Arial", 22, "bold"),
            fg="#00ff9d",
            bg="#0b0f14"
        )

        self.title.pack(side="left", padx=20)

        self.score_label = tk.Label(
            self.header,
            text="SCORE: 0",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="#0b0f14"
        )

        self.score_label.pack(side="right", padx=20)

        # Canvas
        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg="#111820",
            highlightthickness=0
        )

        self.canvas.pack(padx=15, pady=10)

        # Bottom
        self.bottom = tk.Frame(
            root,
            bg="#0b0f14"
        )

        self.bottom.pack(fill="x", pady=10)

        self.info = tk.Label(
            self.bottom,
            text="W A S D  /  ARROW KEYS",
            font=("Arial", 11, "bold"),
            fg="#778899",
            bg="#0b0f14"
        )

        self.info.pack()

        # Keyboard
        self.root.bind("<KeyPress>", self.key_pressed)

        self.show_start_screen()

    # =========================
    # START SCREEN
    # =========================

    def show_start_screen(self):

        self.canvas.delete("all")

        self.canvas.create_text(
            WIDTH // 2,
            180,
            text="NEON",
            fill="#00ff9d",
            font=("Arial", 55, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            240,
            text="SNAKE",
            fill="white",
            font=("Arial", 55, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            320,
            text="Eat • Grow • Survive",
            fill="#718096",
            font=("Arial", 16)
        )

        self.canvas.create_text(
            WIDTH // 2,
            400,
            text="PRESS SPACE TO START",
            fill="#00ff9d",
            font=("Arial", 18, "bold")
        )

        self.root.bind("<space>", self.start_game)

    # =========================
    # START GAME
    # =========================

    def start_game(self, event=None):

        self.root.unbind("<space>")

        self.snake = [
            [10, 10],
            [9, 10],
            [8, 10]
        ]

        self.direction = "Right"
        self.next_direction = "Right"

        self.food = self.create_food()

        self.score = 0

        self.running = True

        self.score_label.config(
            text="SCORE: 0"
        )

        self.game_loop()

    # =========================
    # FOOD
    # =========================

    def create_food(self):

        while True:

            food = [
                random.randint(0, COLS - 1),
                random.randint(0, ROWS - 1)
            ]

            if food not in self.snake:
                return food

    # =========================
    # KEYBOARD
    # =========================

    def key_pressed(self, event):

        key = event.keysym.lower()

        directions = {
            "w": "Up",
            "up": "Up",

            "s": "Down",
            "down": "Down",

            "a": "Left",
            "left": "Left",

            "d": "Right",
            "right": "Right"
        }

        if key not in directions:
            return

        new_direction = directions[key]

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        if new_direction != opposite[self.direction]:

            self.next_direction = new_direction

    # =========================
    # GAME LOOP
    # =========================

    def game_loop(self):

        if not self.running:
            return

        self.direction = self.next_direction

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= 1

        elif self.direction == "Down":
            head_y += 1

        elif self.direction == "Left":
            head_x -= 1

        elif self.direction == "Right":
            head_x += 1

        new_head = [head_x, head_y]

        # Wall collision
        if (
            head_x < 0
            or head_x >= COLS
            or head_y < 0
            or head_y >= ROWS
        ):

            self.game_over()
            return

        # Body collision
        if new_head in self.snake:

            self.game_over()
            return

        # Move
        self.snake.insert(0, new_head)

        # Food
        if new_head == self.food:

            self.score += 10

            self.score_label.config(
                text=f"SCORE: {self.score}"
            )

            self.food = self.create_food()

        else:

            self.snake.pop()

        self.draw()

        self.root.after(
            SPEED,
            self.game_loop
        )

    # =========================
    # DRAW
    # =========================

    def draw(self):

        self.canvas.delete("all")

        # Grid
        for x in range(0, WIDTH, CELL):

            self.canvas.create_line(
                x,
                0,
                x,
                HEIGHT,
                fill="#18222c"
            )

        for y in range(0, HEIGHT, CELL):

            self.canvas.create_line(
                0,
                y,
                WIDTH,
                y,
                fill="#18222c"
            )

        # Food glow
        fx, fy = self.food

        x1 = fx * CELL
        y1 = fy * CELL

        self.canvas.create_oval(
            x1 + 5,
            y1 + 5,
            x1 + CELL - 5,
            y1 + CELL - 5,
            fill="#ff3366",
            outline="#ff6688",
            width=2
        )

        # Snake
        for i, segment in enumerate(self.snake):

            x, y = segment

            x1 = x * CELL
            y1 = y * CELL

            x2 = x1 + CELL
            y2 = y1 + CELL

            if i == 0:

                # Head
                self.canvas.create_rectangle(
                    x1 + 2,
                    y1 + 2,
                    x2 - 2,
                    y2 - 2,
                    fill="#00ff9d",
                    outline="#7affc8",
                    width=2
                )

                # Eyes
                self.draw_eyes(
                    x1,
                    y1
                )

            else:

                # Body
                self.canvas.create_rectangle(
                    x1 + 3,
                    y1 + 3,
                    x2 - 3,
                    y2 - 3,
                    fill="#00c982",
                    outline="#00ff9d"
                )

    # =========================
    # EYES
    # =========================

    def draw_eyes(self, x, y):

        positions = {
            "Right": [(20, 8), (20, 20)],
            "Left": [(8, 8), (8, 20)],
            "Up": [(8, 8), (20, 8)],
            "Down": [(8, 20), (20, 20)]
        }

        for ex, ey in positions[self.direction]:

            self.canvas.create_oval(
                x + ex - 3,
                y + ey - 3,
                x + ex + 3,
                y + ey + 3,
                fill="black"
            )

    # =========================
    # GAME OVER
    # =========================

    def game_over(self):

        self.running = False

        self.canvas.create_rectangle(
            0,
            0,
            WIDTH,
            HEIGHT,
            fill="#080b10"
        )

        self.canvas.create_text(
            WIDTH // 2,
            220,
            text="GAME OVER",
            fill="#ff3366",
            font=("Arial", 48, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            290,
            text=f"SCORE  {self.score}",
            fill="white",
            font=("Arial", 22, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            360,
            text="PRESS R TO RESTART",
            fill="#00ff9d",
            font=("Arial", 16, "bold")
        )

        self.root.bind(
            "<r>",
            self.restart
        )

        self.root.bind(
            "<R>",
            self.restart
        )

    # =========================
    # RESTART
    # =========================

    def restart(self, event=None):

        self.root.unbind("<r>")
        self.root.unbind("<R>")

        self.start_game()


# =========================
# RUN
# =========================

root = tk.Tk()

game = SnakeGame(root)

root.mainloop()
