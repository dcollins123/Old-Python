from random import choice, randrange
from string import ascii_lowercase, ascii_uppercase
import turtle

from freegames import vector

# Combine lowercase and uppercase letters
all_letters = ascii_lowercase + ascii_uppercase
targets = []
letters = []
score = 0

def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200

def draw():
    """Draw letters."""
    turtle.clear()

    for target, letter in zip(targets, letters):
        turtle.goto(target.x, target.y)
        turtle.write(letter, align='center', font=('Consolas', 20, 'normal'))

    turtle.update()

def move():
    """Move letters."""
    global score
    if randrange(20 - min(15, score // 5)) == 0:
        x = randrange(-150, 150)
        target = vector(x, 200)
        targets.append(target)
        letter = choice(all_letters)
        letters.append(letter)

    # Move the letters downwards
    for target in targets:
        target.y -= 0.5 * (1 + score / 10)

    # Draw the letters on screen
    draw()

    # Remove letters that have moved off screen
    targets_to_remove = [target for target in targets if not inside(target)]
    for target in targets_to_remove:
        targets.remove(target)
        del letters[targets.index(target)]

    # Make the game faster as the score gets higher
    turtle.ontimer(move, 100 - min(90, score))

def press(key):
    """Detect key press and remove corresponding letter from screen."""
    global score
    # Convert to lowercase because letters list contains lowercase
    key = key.lower()
    if key in letters:
        score += 1
        index = letters.index(key)
        del targets[index]
        del letters[index]
    else:
        score -= 1
    print('Score:', score)

# Set up the screen
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)

# Listen for key presses
turtle.listen()
for letter in ascii_lowercase:
    turtle.onkey(lambda letter=letter: press(letter), letter)          # Lowercase
    turtle.onkey(lambda letter=letter: press(letter.upper()), letter)  # Uppercase

# Start the game
move()
turtle.done()
