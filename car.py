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

    left_img = None
    right_img = None

    def __init__(self, group, size):
        super().__init__(group)
        if Car.right_img is None:
            Car.right_img = load_image('car2.png')
            Car.left_img = pygame.transform.flip(Car.right_img, True, False)
        self.width, self.height = size
        self.img = Car.right_img
        self.rect = self.img.get_rect()
        self.speed = 1
        self.ticks = 0

    def update(self):
        if self.rect.left + self.rect.width > self.width or self.rect.left < 0:
            self.speed = -self.speed
        if self.speed > 0:
            self.img = Car.right_img
        else:
            self.img = Car.left_img
        self.rect.left = self.rect.left + self.speed
        self.ticks = 0


def main():
    size = 600, 100
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Машинка')
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
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