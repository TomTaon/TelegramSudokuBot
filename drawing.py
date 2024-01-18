import pygame

# this code generates sudoku board image using pygame and saves it to "board.jpg

# os.environ["SDL_VIDEODRIVER"] = "dummy"

LABELS = ("A", "B", "C", "D", "E", "F", "G", "H", "I")

lines_color = "black"
background_color = "light gray"
text_color = "black"
window_size = 550

# initializing pygame's functionality
pygame.init()

# initialize window
screen = pygame.display.set_mode((window_size, window_size))

# fill in background with color
screen.fill(background_color)

# dif is space between lines, shift is space form upper left corner
# window_size should be (dif*9 + 2*shift)
dif = 50
shift = 50

# drawing sudoku grid
for i in range(10):
    if i % 3 == 0:
        thick = 5
    else:
        thick = 2

    pygame.draw.line(screen,
                     lines_color,
                     (shift, (i * dif) + shift),
                     (dif * 9 + shift, i * dif + shift),
                     thick
                     )

    pygame.draw.line(screen,
                     lines_color,
                     (i * dif + shift, shift),
                     (i * dif + shift, dif * 9 + shift),
                     thick
                     )

    pygame.display.update()

# setting up font for labels
font = pygame.font.SysFont("arial", 40)

# drawing signs for rows and columns
for i, value in enumerate(LABELS):
    text = font.render(value, True, text_color, None)
    screen.blit(text, (65 + dif * i, 0))
    pygame.display.update()

for i in range(1, 10):
    text = font.render(str(i), True, text_color, None)
    screen.blit(text, (17, 54 + dif * (i - 1)))
    pygame.display.update()

pygame.image.save(screen, "board.jpeg")

# ######################################################################################################################################

# this part of code is some pygame library testing not related to the project

left = 0
right = 0
up = 0
down = 0

inputs_counter = 0
run = True


# prints current state of arrow keys, 1 - means pressed, 0 - not pressed
def print_arrows_state(l, r, u, d):
    print(f"#{u}#\n"
          f"{l}{d}{r}")
    print("---------")


# event handler loop
while run:

    # Loop through the events stored in event.get()
    for event in pygame.event.get():

        '''
        inputs_counter += 1
        print(f"got input nr: {inputs_counter}")
        '''

        # Quit button event closes window
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
            print("enough")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = 1
            elif event.key == pygame.K_RIGHT:
                right = 1
            elif event.key == pygame.K_UP:
                up = 1
            elif event.key == pygame.K_DOWN:
                down = 1
            print_arrows_state(left, right, up, down)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = 0
            elif event.key == pygame.K_RIGHT:
                right = 0
            elif event.key == pygame.K_UP:
                up = 0
            elif event.key == pygame.K_DOWN:
                down = 0
            print_arrows_state(left, right, up, down)
