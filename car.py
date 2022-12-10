import os
import pygame
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


class Car(pygame.sprite.Sprite):

    image_left = None
    image_right = None

    def __init__(self, group, size):
        super().__init__(group)
        if Car.image_right is None:
            Car.image_right = load_image('car2.png')
            Car.image_left = pygame.transform.flip(Car.image_right, True, False)
        self.width, self.height = size
        self.image = Car.image_right
        self.rect = self.image.get_rect()
        self.speed = 1
        self.ticks = 0

    def update(self):
        if self.rect.left + self.rect.width > self.width or self.rect.left < 0:
            self.speed = -self.speed
        if self.speed > 0:
            self.image = Car.image_right
        else:
            self.image = Car.image_left
        self.rect.left = self.rect.left + self.speed
        self.ticks = 0
        self.image = self.image


def main():
    size = 600, 100
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Машинка')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    _ = Car(all_sprites, size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color(255, 255, 255))   
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()



if __name__ == '__main__':
    main()