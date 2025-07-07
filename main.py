import pygame
import math
import sys
import basic
import basic_coa
import basic_dms

# Initialize Pygame
pygame.init()

# Set up the initial screen dimensions
screen_width = 1365
screen_height = 710
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Set the title of the window
pygame.display.set_caption("Hangman")

# Load background images
background_image_1 = pygame.image.load('desk.jpg')  # Change 'background1.jpg' to your image file path for first screen
background_image_2 = pygame.image.load('1.png')       # Change 'background2.jpg' to your image file path for second screen
nested_screen1_image = pygame.image.load('desk.jpg') # Change 'nested_screen1.jpg' to your image file path for nested screen 1
nested_screen2_image = pygame.image.load('desk.jpg')  # Change 'nested_screen2.jpg' to your image file path for nested screen 2
nested_screen3_image = pygame.image.load('desk.jpg')  # Change 'nested_screen3.jpg' to your image file path for nested screen 3


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define Button class
class Button:
    def __init__(self, text, image_path, position, size):
        self.text = text
        self.image_path = image_path
        self.image = pygame.image.load(image_path).convert_alpha() if image_path else None
        self.image = pygame.transform.scale(self.image, size) if self.image else None
        self.position = position
        self.size = size
        self.font = pygame.font.Font("Lacquer-Regular.ttf", 75)  # Change "Lacquer-Regular.ttf" to the path of your font file

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.position)
        else:
            transparent_surface = pygame.Surface(self.size, pygame.SRCALPHA)
            transparent_surface.fill((0, 0, 0, 0))  # Fill with transparent color
            screen.blit(transparent_surface, self.position)
            text_surface = self.font.render(self.text, True, WHITE)
            text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2))
            screen.blit(text_surface, text_rect)
# Create buttons for first screen
next_button_screen1 = Button(" ", 'start_btn.png', (screen_width - 750, screen_height - 600), (300, 150))
exit_button_screen1 = Button(" ", 'exit_btn.png', (screen_width - 350, screen_height - 600), (300, 150))

# Create buttons for second screen
next_button1_screen2 = Button("DSA", None, (screen_width - 1250, screen_height - 600), (300, 150))

next_button2_screen2 = Button("DBMS", None, (screen_width  - 800, screen_height - 600), (300, 150))
next_button3_screen2 = Button("COA", None, (screen_width  - 350, screen_height - 600), (300, 150))
back_button_screen2 = Button(" ", 'back1.png', (1220, screen_height - 700), (90, 50))
back_button_nested_screen1 = Button(" ", 'back1.png', (1220, screen_height - 700), (90, 50))
back_button_nested_screen2 = Button(" ", 'back1.png', (1220, screen_height - 700), (90, 50))
back_button_nested_screen3 = Button(" ", 'back1.png', (1220, screen_height - 700), (90, 50))

# Load sound files for each nested screen
sound_nested_screen1 = pygame.mixer.Sound('coa.mp3')  # Change 'sound_nested_screen1.wav' to the path of your sound file for nested screen 1
sound_nested_screen2 = pygame.mixer.Sound('dms.mp3')  # Change 'sound_nested_screen2.wav' to the path of your sound file for nested screen 2
sound_nested_screen3 = pygame.mixer.Sound('Dsa.mp3')  # Change 'sound_nested_screen3.wav' to the path of your sound file for nested screen 3
sound_screen1 = pygame.mixer.Sound('B.mp3')  # Change 'sound_screen1.wav' to the path of your sound file for screen 1
sound_screen2 = pygame.mixer.Sound('B.mp3')  # Change 'sound_screen2.wav' to the path of your sound file for screen 2
click_sound = pygame.mixer.Sound('A.mp3')  # Change 'click_sound.wav' to the path of your click sound file


# Define screen constants for nested screens
NESTED_SCREEN_1 = 1
NESTED_SCREEN_2 = 2
NESTED_SCREEN_3 = 3

def play_sound_nested_screen(screen_type):
    if screen_type == NESTED_SCREEN_1:
        sound_nested_screen1.play()
    elif screen_type == NESTED_SCREEN_2:
        sound_nested_screen2.play()
    elif screen_type == NESTED_SCREEN_3:
        sound_nested_screen3.play()


# Function to handle button clicks for first screen
def handle_button_click_screen1(mouse_pos):
    if next_button_screen1.position[0] < mouse_pos[0] < next_button_screen1.position[0] + next_button_screen1.size[0] and \
            next_button_screen1.position[1] < mouse_pos[1] < next_button_screen1.position[1] + next_button_screen1.size[1]:
        click_sound.play()
        return 1
    elif exit_button_screen1.position[0] < mouse_pos[0] < exit_button_screen1.position[0] + exit_button_screen1.size[0] and \
            exit_button_screen1.position[1] < mouse_pos[1] < exit_button_screen1.position[1] + exit_button_screen1.size[1]:
        click_sound.play()
        pygame.quit()
        sys.exit()
    return 0


# Function to handle button clicks for second screen
def handle_button_click_screen2(mouse_pos):
    if next_button1_screen2.position[0] < mouse_pos[0] < next_button1_screen2.position[0] + next_button1_screen2.size[0] and \
            next_button1_screen2.position[1] < mouse_pos[1] < next_button1_screen2.position[1] + next_button1_screen2.size[1]:
        click_sound.play()
        return NESTED_SCREEN_1
    elif next_button2_screen2.position[0] < mouse_pos[0] < next_button2_screen2.position[0] + next_button2_screen2.size[0] and \
            next_button2_screen2.position[1] < mouse_pos[1] < next_button2_screen2.position[1] + next_button2_screen2.size[1]:
        click_sound.play()
        return NESTED_SCREEN_2
    elif next_button3_screen2.position[0] < mouse_pos[0] < next_button3_screen2.position[0] + next_button3_screen2.size[0] and \
            next_button3_screen2.position[1] < mouse_pos[1] < next_button3_screen2.position[1]+next_button3_screen2.size[1]:
        click_sound.play()
        return NESTED_SCREEN_3
    elif back_button_screen2.position[0] < mouse_pos[0] < back_button_screen2.position[0] + back_button_screen2.size[0] and \
            back_button_screen2.position[1] < mouse_pos[1] < back_button_screen2.position[1] + back_button_screen2.size[1]:
        click_sound.play()
        return -1  # Negative value to represent back button
    return 0
def handle_button_click_nested_screen(screen_type, mouse_pos):
    if screen_type is None:
        return 0
    elif screen_type == NESTED_SCREEN_1:
        if back_button_nested_screen1.position[0] < mouse_pos[0] < back_button_nested_screen1.position[0] + back_button_nested_screen1.size[0] and \
                back_button_nested_screen1.position[1] < mouse_pos[1] < back_button_nested_screen1.position[1] + back_button_nested_screen1.size[1]:
            return -1  # Indicates back button is clicked
    elif screen_type == NESTED_SCREEN_2:
        if back_button_nested_screen2.position[0] < mouse_pos[0] < back_button_nested_screen2.position[0] + back_button_nested_screen2.size[0] and \
                back_button_nested_screen2.position[1] < mouse_pos[1] < back_button_nested_screen2.position[1] + back_button_nested_screen2.size[1]:
            return -1  # Indicates back button is clicked
    elif screen_type == NESTED_SCREEN_3:
        if back_button_nested_screen3.position[0] < mouse_pos[0] < back_button_nested_screen3.position[0] + back_button_nested_screen3.size[0] and \
                back_button_nested_screen3.position[1] < mouse_pos[1] < back_button_nested_screen3.position[1] + back_button_nested_screen3.size[1]:
            return -1  # Indicates back button is clicked
    return 0


# Main loop
current_screen = 1  # Start with the first screen
current_nested_screen = None  # No nested screen initially
sound_channel_screen1 = None  # Sound channel for screen 1
sound_channel_screen2 = None  # Sound channel for screen 2
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update screen dimensions if window is resized
            screen_width, screen_height = event.dict['size']
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if current_screen == 1:
                result = handle_button_click_screen1(mouse_pos)
                if result == 1:
                    current_screen = 2
                    if sound_channel_screen2 is not None:
                        sound_channel_screen2.stop()  # Stop sound playback for screen 2
                    sound_channel_screen1 = sound_screen1.play()  # Play sound for screen 1
            elif current_screen == 2:
                if current_nested_screen is None:
                    result = handle_button_click_screen2(mouse_pos)
                    if result == NESTED_SCREEN_1:
                        current_nested_screen = NESTED_SCREEN_1
                        if sound_channel_screen1 is not None:
                            sound_channel_screen1.stop()  # Stop sound playback for screen 1
                        sound_channel_screen2 = sound_nested_screen1.play()  # Play sound for nested screen 1
                    elif result == NESTED_SCREEN_2:
                        current_nested_screen = NESTED_SCREEN_2
                        if sound_channel_screen1 is not None:
                            sound_channel_screen1.stop()  # Stop sound playback for screen 1
                        sound_channel_screen2 = sound_nested_screen2.play()  # Play sound for nested screen 2
                    elif result == NESTED_SCREEN_3:
                        current_nested_screen = NESTED_SCREEN_3
                        if sound_channel_screen1 is not None:
                            sound_channel_screen1.stop()  # Stop sound playback for screen 1
                        sound_channel_screen2 = sound_nested_screen3.play()  # Play sound for nested screen 3
                    elif result == -1:
                        current_screen = 1  # Go back to the first screen
                        if sound_channel_screen1 is not None:
                            sound_channel_screen1.stop()  # Stop sound playback for screen 1
                else:
                    result = handle_button_click_nested_screen(current_nested_screen, mouse_pos)
                    if result == -1:
                        current_nested_screen = None  # Close the nested screen
                        if sound_channel_screen2 is not None:
                            sound_channel_screen2.stop()  # Stop sound playback for screen 2
                        sound_channel_screen1 = sound_screen2.play()  # Play sound for screen 2
                    
                        
    # Draw current screen
    if current_screen == 1:
        screen.blit(pygame.transform.scale(background_image_1, (screen_width, screen_height)), (0, 0))
        next_button_screen1.draw(screen)
        exit_button_screen1.draw(screen)
    elif current_screen == 2:
        screen.blit(pygame.transform.scale(background_image_2, (screen_width, screen_height)), (0, 0))
        next_button1_screen2.draw(screen)
        next_button2_screen2.draw(screen)
        next_button3_screen2.draw(screen)
        back_button_screen2.draw(screen)

        if current_nested_screen is not None:
            # Draw nested screen based on current_nested_screen value
            if current_nested_screen == NESTED_SCREEN_1:
                #screen.blit(pygame.transform.scale(nested_screen1_image, (screen_width, screen_height)), (0, 0))                                                         
                basic.main()
                back_button_nested_screen1.draw(screen)
            elif current_nested_screen == NESTED_SCREEN_2:
                screen.blit(pygame.transform.scale(nested_screen2_image, (screen_width, screen_height)), (0, 0))
                basic_coa.main()
                back_button_nested_screen2.draw(screen)
            elif current_nested_screen == NESTED_SCREEN_3:
                screen.blit(pygame.transform.scale(nested_screen3_image, (screen_width, screen_height)), (0, 0))
                basic_dms.main()
                back_button_nested_screen3.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()