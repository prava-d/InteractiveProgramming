"""
Author: Prava Dhulipalla
Display candidate names on a circle and show the candidate's
details in a popup when mouse is on the candidate's name
"""

import pygame
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


def show_candidates(screen, candidates):
    """
    Display candidates names and returns screen position details
    """
    screen_pos = []

    # Define some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (0, 0 , 0)
    green = (255, 250, 240)
    blue = (0, 0, 0)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    gray = (255, 250, 240)

    # Screen width and height
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # First draw a circle
    center = (int(screen_width/2), int(screen_height/2))
    radius = int(screen_height * 0.3)
    width = int(screen_height * 0.02)
    pygame.draw.circle(screen, green, center, radius, width)

    # Select the font to use, size, bold, italics
    font_size = int(screen_height * 0.03)
    font = pygame.font.SysFont('Calibri', font_size, True, False)

    a = 0
    for candidate in candidates:
        # Name length on screen in pixels (approx)
        name_len = int(len(candidate[0]) * font_size / 2)

        angle = a * 2 * math.pi/len(candidates)

        # Find screen position to write names around the circle
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))

        # Draw a small red circle
        pygame.draw.circle(screen, red, [x, y], 4)

        # Calculate the position for writing name on the screen
        if x < center[0]:
            x -= name_len
        elif x == center[0]:
            x -= int(name_len / 2)

        if y < center[1]:
            y -= font_size
        elif y == center[1]:
            y -= int(font_size / 2)

        # Draw the text
        rect = pygame.Rect(x, y, name_len, font_size)
        screen_pos.append((candidate[0], candidate[1], candidate[2], rect))
        #pygame.draw.rect(screen, WHITE, rect, 0)
        t = font.render(candidate[0], True, blue)
        screen.blit(t, [x, y])
        a += 1

    return screen_pos


def show_popup(screen, candidate):
    """
    Display candidate's details
    """
    # Define some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0 , 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    win_color = (255, 250, 240)
    text_color = (0, 0, 0)

    # Screen width and height
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # popup window
    w = screen_width / 1.9
    x = (screen_width - w) / 2
    h = screen_height / 1.8
    y = (screen_height - h) / 2
    pygame.draw.rect(screen, win_color, (x, y, w, h), 0)

    # Photo
    photo_size = (int(screen_height / 7), int(screen_height / 7))
    image = pygame.image.load(candidate[1]).convert()
    image = pygame.transform.scale(image, photo_size)
    screen.blit(image, [int(x * 1.2), int(y * 1.1)])

    # Name
    nx = int(x * 1.7)
    ny = int(y * 1.3)
    font_size = int(screen_height * 0.03)
    font = pygame.font.SysFont('Calibri', font_size, True, False)
    t = font.render(candidate[0], True, red)
    screen.blit(t, [nx, ny])

    # Details
    x = int(x * 1.1)
    y = int(y * 1.8)
    font_size = int(screen_height * 0.035)
    line_size = int(screen_height * 0.06)
    font = pygame.font.SysFont('Calibri', font_size, False, False)
    text = candidate[2]
    while len(text) > 0:
        if len(text) > line_size:
            line = text[0:line_size]
            text = text[line_size:]
        else:
            line = text
            text = ''

        t = font.render(line.strip(), True, text_color)
        screen.blit(t, [x, y])
        y += font_size

def legend(screen,texty):
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0 , 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    win_color = (255, 250, 240)
    text_color = (0, 0, 0)

    # Screen width and height
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # popup window
    #w = screen_width / 3
    x = 0 #(screen_width - w) / 2
    #h = screen_height / 1.8
    y = 0#(screen_height - h) / 2
    #pygame.draw.rect(screen, win_color, (x, y, w, h), 0)


    # Details
    x = int(x * 1.1)
    y = int(y * 1.8)
    font_size = int(screen_height * 0.035)
    line_size = int(screen_height * 0.06)
    font = pygame.font.SysFont('Calibri', font_size, False, False)
    text = texty
    greenBox = pygame.Rect(0,0,100,100)
    pygame.draw.rect(screen, green, greenBox)
    while len(text) > 0:
       if len(text) > line_size:
           line = text[0:line_size]
           text = text[line_size:]
       else:
           line = text
           text = ''
    t = font.render(line.strip(), True, text_color)
    #    screen.blit(t, [x, y])
    #    y += font_size
#def goodness_meter(phases)
    #if
#return good
def lines(dis):
    if dis<=1:
        return "red"
    if dis>=1:
        return "green"
    if dis==0:
        return "black"

def main():
    """
    This is our main program.
    """

    candidates = [
    ('Bernie Sanders',
     'Bernie Sanders.jpg',
     'Bernard "Bernie" Sanders is an American politician who has been the junior United States Senator from Vermont since 2007. Sanders is the longest serving independent in U.S. congressional history.'),
    ('Hillary Clinton',
     'Hillary Clinton.jpg',
     'Hillary Diane Rodham Clinton is an American politician who was the 67th United States Secretary of State from 2009 to 2013, U.S. Senator from New York from 2001 to 2009, First Lady of the United States'),
    ('Donald Trump',
     'Donald Trump.jpg',
     'Donald John Trump is an American businessman, television personality, politician, and the 45th President of the United States.'),
    ('Ted Cruz',
     'Ted Cruz.jpg',
     'Rafael Edward "Ted" Cruz is an American politician and attorney, who has served as the junior United States Senator from Texas since 2013. He was a candidate for the Republican nomination for President of the United States in the 2016 election.'),
    ('Marco Rubio',
     'Marco Rubio.jpg',
     'Marco Antonio Rubio is an American politician and attorney, and the junior United States Senator from Florida. Rubio previously served as Speaker of the Florida House of Representatives.'),
    ('Jeb Bush',
     'Jeb Bush.jpg',
     'John Ellis "Jeb" Bush Sr. is an American businessman and politician who served as the 43rd Governor of Florida from 1999 to 2007.'),
    ('John Kasich',
     'John Kasich.jpg',
     'John Richard Kasich is an American politician and former television host. He is the 69th and current Governor of Ohio. First elected in 2010 and re-elected in 2014, Kasich is a member of the Republican Party.'),
    ('Ben Carson',
     'Ben Carson.jpg',
     'Benjamin Solomon "Ben" Carson Sr. is an American neurosurgeon, author, and politician who is the 17th and current United States Secretary of Housing and Urban Development, under the Trump Administration.')
    ]

    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('bettermap.png').convert()
    background = pygame.transform.scale(background, size)

    pygame.display.set_caption("2016 Presidential Candidates")



    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    screen.blit(background, background.get_rect())
    screen_pos = show_candidates(screen, candidates)

    while not done:

        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEMOTION:
                on_candidate = False
                p = pygame.mouse.get_pos()
                for candidate in screen_pos:
                    if candidate[3].collidepoint(p):
                        show_popup(screen, candidate)
                        on_candidate = True
                if not on_candidate:
                    screen.blit(background, background.get_rect())
                    legend_local = legend(screen,"Positve Negative Netural")
                    screen_pos = show_candidates(screen, candidates)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(10)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
