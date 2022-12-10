import os
import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('hero_move', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def character():
    size = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Герой двигается')
    all_sprites = pygame.sprite.Group()
    cursor_image = load_image('creature.png')
    character = pygame.sprite.Sprite(all_sprites)
    character.image = cursor_image
    character.rect = character.image.get_rect()
    step = 10
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                character.rect.top += step
            elif key[pygame.K_UP]:
                character.rect.top -= step
            if key[pygame.K_RIGHT]:
                character.rect.right += step
            if key[pygame.K_LEFT]:
                character.rect.left += step
    
        screen.fill(pygame.Color(255, 255, 255))   
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()



if __name__ == '__main__':
    sys.exit(character())
