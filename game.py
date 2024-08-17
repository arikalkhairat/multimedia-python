import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

image = pygame.image.load('image.png')
sound = pygame.mixer.Sound('result.wav')

sound.play()

x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 1
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 50))

    # Memperbarui tampilan
    pygame.display.flip()

# Mengakhiri pygame
pygame.quit()
