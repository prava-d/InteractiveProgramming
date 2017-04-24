"""
Display candidate names on a circle and show the candidate's
sentiments when mouse is on the candidate's name
"""

import pygame
import math
import pickle
import phrase_extractor as pe

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Define some colors
RED     = (255, 0 , 0)
BLUE    = (0, 0, 255)
POWDER_BLUE = (176, 224, 230)
FIREBRICK = (178, 34, 34)

# Define colors for sentiment
NEGATIVE = (255, 0 , 0)    # red
POSITIVE = (0, 225, 0)     # green
NEUTRAL  = (125, 125, 125) # gray
NO_INFO  = (0, 255, 255)   # cyan

class Candidate:
    def __init__(self, name, image_file, pickle_file):
        self.name = name
        self.picture = image_file
        f = open(pickle_file, 'rb')
        self.quotes = pickle.load(f)
        f.close()
        self.sentiment = []
        self.screen_rect = None
        self.screen_xy = None

    def update_sentiment(self, candidate):
        names = candidate.name.split()
        names.append(candidate.name)

        sentences = []
        for quote in self.quotes:
            sentences += pe.get_sentences(quote, names)

        score = 0
        mood = NO_INFO
        for s in sentences:
            quote = pe.get_quote(s)
            score += quote.tone
        if len(sentences) > 0:
            if score > 0:
                mood = POSITIVE
            elif score < 0:
                mood = NEGATIVE
            else:
                mood = NEUTRAL
        self.sentiment.append((candidate, mood))


def get_sentiments(candidates):
    """
    Update sentiments for all candidates
    """
    for candidate1 in candidates:
        for candidate2 in candidates:
            if candidate1 != candidate2:
                candidate1.update_sentiment(candidate2)


def show_sentiments(screen, candidate):
    """
    Show sentiment lines for the candidate
    """
    # Screen width and height
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Photo
    photo_size = (int(screen_height / 7), int(screen_height / 6))
    image = pygame.image.load(candidate.picture).convert()
    image = pygame.transform.scale(image, photo_size)
    screen.blit(image, [10, 10])

    # lines
    for (to_candidate, mood) in candidate.sentiment:
        pygame.draw.line(screen, mood, candidate.screen_xy, to_candidate.screen_xy, 2)


def show_candidates(screen, candidates):
    """
    Display candidates names and returns screen position details
    """
    # Screen width and height
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Display legend
    font_size = int(screen_height * 0.02)
    font = pygame.font.SysFont('Calibri', font_size, True, False)

    x = int(screen_width * 0.85)
    y = int(screen_height - 11 * font_size)
    t = font.render('Legend:', True, BLUE)
    screen.blit(t, [x, y])

    x = int(screen_width * 0.9)
    y = int(screen_height - 10 * font_size)
    t = font.render('Positive', True, POSITIVE)
    screen.blit(t, [x, y])

    y = int(screen_height - 9 * font_size)
    t = font.render('Negative', True, NEGATIVE)
    screen.blit(t, [x, y])

    y = int(screen_height - 8 * font_size)
    t = font.render('Neutral', True, NEUTRAL)
    screen.blit(t, [x, y])

    y = int(screen_height - 7 * font_size)
    t = font.render('No Info', True, NO_INFO)
    screen.blit(t, [x, y])

    # Draw a circle
    center = (int(screen_width/2), int(screen_height/2))
    radius = int(screen_height * 0.4)
    width = int(screen_height * 0.02)
    pygame.draw.circle(screen, FIREBRICK, center, radius, width)

    # Select the font to use, size, bold, italics
    font_size = int(screen_height * 0.03)
    font = pygame.font.SysFont('Calibri', font_size, True, False)

    a = 0
    for candidate in candidates:
        # Name length on screen in pixels (approx)
        name_len = int(len(candidate.name) * font_size / 2)

        angle = a * 2 * math.pi/len(candidates)

        # Find screen position to write names around the circle
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))

        # Draw a small red circle
        candidate.screen_xy = (x,y)
        pygame.draw.circle(screen, POWDER_BLUE, candidate.screen_xy, 5)

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
        candidate.screen_rect = pygame.Rect(x, y, name_len, font_size)
        t = font.render(candidate.name, True, POWDER_BLUE)
        screen.blit(t, [x, y])
        a += 1


def show_popup(screen, candidate):
    """
    Display candidate's details
    """
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
    image = pygame.image.load(candidate.picture).convert()
    image = pygame.transform.scale(image, photo_size)
    screen.blit(image, [int(x * 1.2), int(y * 1.1)])

    # Name
    nx = int(x * 1.7)
    ny = int(y * 1.3)
    font_size = int(screen_height * 0.03)
    font = pygame.font.SysFont('Calibri', font_size, True, False)
    t = font.render(candidate.name, True, RED)
    screen.blit(t, [nx, ny])

    # Details
    x = int(x * 1.1)
    y = int(y * 1.8)
    font_size = int(screen_height * 0.035)
    line_size = int(screen_height * 0.06)
    font = pygame.font.SysFont('Calibri', font_size, False, False)
    text = candidate.quotes[0]
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



def main():
    """
    This is our main program.
    """

    candidates = [
        Candidate('Bernie Sanders', 'Bernie Sanders.jpg', 'bernietwitters.pickle'),
        Candidate('Hillary Clinton', 'Hillary Clinton.jpg', 'clintontwitters.pickle'),
        Candidate('Ted Cruz', 'Ted Cruz.jpg', 'cruztwitters.pickle'),
        Candidate('Tim Kaine', 'Tim Kaine.jpg', 'kainetwitters.pickle'),
        Candidate('John Kasich', 'John Kasich.jpg', 'kasichtwitters.pickle'),
        Candidate('Martin O\'Malley', 'Martin O\'Malley.jpg', 'malleytwitters.pickle'),
        Candidate('Mike Pence', 'Mike Pence.jpg', 'pencertwitter.pickle'),
        Candidate('Donald Trump', 'Donald Trump.jpg', 'trumptwitters.pickle')
        ]

    get_sentiments(candidates)

    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('background.jpg').convert()
    background = pygame.transform.scale(background, size)

    pygame.display.set_caption("2016 Presidential Candidates")



    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    screen.blit(background, background.get_rect())
    show_candidates(screen, candidates)

    while not done:

        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEMOTION:
                on_candidate = False
                p = pygame.mouse.get_pos()
                for candidate in candidates:
                    if candidate.screen_rect.collidepoint(p):
                        #show_popup(screen, candidate)
                        show_sentiments(screen, candidate)
                        on_candidate = True
                if not on_candidate:
                    screen.blit(background, background.get_rect())
                    show_candidates(screen, candidates)

        # --- Wrap-up
        # Limit to 10 frames per second
        clock.tick(10)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
