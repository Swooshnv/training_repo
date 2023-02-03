from pygame.locals import *
import pygame

class player:
    x = y = 10
    speed = 1

    def right(self):
        self.x = self.x + self.speed
    def left(self):
        self.x = self.x - self.speed
    def down(self):
        self.y = self.y + self.speed
    def up(self):
        self.y = self.y - self.speed
    
class window:
    width = 1000
    height = 700
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = player()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)

        pygame.display.set_caption('PyGame Practice')
        self._running = True
        self._image_surf = pygame.image.load("D:/studies/coding/pygame/what.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(( 0, 0, 0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if self.player.x >= 0 and self.width - self._image_surf.get_width() >= self.player.x and self.player.y >= 0 and self.height - self._image_surf.get_height() >= self.player.y:
                if (keys[K_LSHIFT]):
                    self.player.speed = 4
                elif (keys[K_LCTRL]):
                    self.player.speed = 0.5
                else:
                    self.player.speed = 1
                if (keys[K_RIGHT]):
                    self.player.right()
                    print(self.player.x)
                if (keys[K_UP]):
                    self.player.up()
                    print(self.player.y)
                if (keys[K_LEFT]):
                    self.player.left()
                    print(self.player.x)
                if (keys[K_DOWN]):
                    self.player.down()
                    print(self.player.y)
            else:
                
                if self.player.x > (self.width - self._image_surf.get_width()):
                    self.player.x = self.width - self._image_surf.get_width()
                elif self.player.x < 0:
                    self.player.x = 0
                elif self.player.y > (self.height - self._image_surf.get_height()):
                    self.player.y = self.height - self._image_surf.get_height()
                elif self.player.y < 0:
                    self.player.y = 0
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = window()
    theApp.on_execute()