import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 600
        self.rect.centery = 700
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self, aliens, bullets):
        aliens.empty
        bullets.empty
        if self.moving_top and self.moving_right\
            and self.rect.right < self.screen_rect.right and self.rect.top > self.screen_rect.top:
            self.center_x += self.ai_settings.ship_speed_factor
            self.center_y -= self.ai_settings.ship_speed_factor
        elif self.moving_left and self.moving_top\
            and self.rect.left > 0 and self.rect.top > self.screen_rect.top:
            self.center_x -= self.ai_settings.ship_speed_factor
            self.center_y -= self.ai_settings.ship_speed_factor
        elif self.moving_left and self.moving_bottom \
                and self.rect.left > 0 and self.rect.bottom < self.screen_rect.bottom:
            self.center_x -= self.ai_settings.ship_speed_factor
            self.center_y += self.ai_settings.ship_speed_factor
        elif self.moving_right and self.moving_bottom \
                and self.rect.right < self.screen_rect.right and self.rect.bottom < self.screen_rect.bottom:
            self.center_x += self.ai_settings.ship_speed_factor
            self.center_y += self.ai_settings.ship_speed_factor
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        elif self.moving_top and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.center_x = 600
        self.center_y = 700

    def blitme(self):
        self.screen.blit(self.image, self.rect)