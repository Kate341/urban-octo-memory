import pygame
import os
import re

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame MP3 Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)
music_folder = "/home/kali/my_project/urban-octo-memory/Lab7"

songs = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]

current_index, is_playing = 0, False

def play_song():
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()
    global is_playing
    is_playing = True

def toggle_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    is_playing = not is_playing

def draw_screen():
    screen.fill(WHITE)
    song_text = f"Now Playing: {os.path.basename(songs[current_index])}"
    screen.blit(font.render(song_text, True, BLACK), (30, 50))

    instructions = [
        "SPACE - Play / Pause", 
        "RIGHT ARROW - Next Song", 
        "LEFT ARROW - Previous Song", 
        "S - Stop", 
        "ESC - Exit"
    ]

    for i, line in enumerate(instructions, start=150):
        screen.blit(small_font.render(line, True, BLUE), (20, i * 40))

    pygame.display.flip()

play_song()
running = True
while running:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_pause()
            elif event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(songs)
                play_song()
            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(songs)
                play_song()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

pygame.quit()