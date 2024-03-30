import random
import turtle
from freegames import vector

score = 0  # Initialize the score

def draw():
    """Draw letters."""
    turtle.clear()
    for target, letter in zip(targets, letters):
        turtle.goto(target.x, target.y)
        turtle.write(letter, align='center', font=('Arial', 20, 'normal'))
    # Display the score
    turtle.goto(-200, 150)
    turtle.write(f"Score: {score}", align='left', font=('Arial', 20, 'normal'))
    turtle.update()

def move():
    """Move letters."""
    global score  # Access the global score variable
    if random.randint(1, 20) == 1:
        x = random.randint(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letters.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    for target in targets:
        target.y -= 5

    # Remove letters that are out of bounds and decrease score
    for i in range(len(targets) - 1, -1, -1):
        if not -200 < targets[i].y < 200:
            del targets[i]
            del letters[i]
            score -= 1  # Decrease the score

    draw()
    turtle.ontimer(move, 100)

def press(key):
    """Press key."""
    global score
    if key in letters:
        i = letters.index(key)
        del targets[i]
        del letters[i]
        score += 1  # Increase the score
    else:
        score -= 1  # Decrease the score for wrong letter

targets = []
letters = []

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.listen()
for letter in 'abcdefghijklmnopqrstuvwxyz':
    turtle.onkey(lambda letter=letter: press(letter), letter)
move()
turtle.done()
