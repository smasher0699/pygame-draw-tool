import pygame
class draw:
    def __init__(self, screen):
        self.screen = screen
        #print("Initialized draw tool")

    def draw_rectangle(self, color, width, height, x, y, thickness = 5):
        shape = pygame.draw.rect(self.screen, color, pygame.Rect(x, y, width, height), width=thickness)
        pygame.display.flip()
        #print("Drew rectangle")
        return shape
    
    def draw_filled_rectangle(self, color, width, height, x, y):
        shape = pygame.draw.rect(self.screen, color, pygame.Rect(x, y, width, height), width=0)
        pygame.Surface.fill(self.screen, color, shape)
        pygame.display.flip()
        #print("Drew filled rectangle")
        return shape

    def draw_square(self, color, width, x, y):
        shape = pygame.draw.rect(self.screen, color, pygame.Rect(x, y, width, width))
        shape.move(x, y)
        pygame.display.flip()
        #print("Drew square")
        return shape
    
    def draw_circle(self, color, radius, location: pygame.Vector2):
        shape = pygame.draw.circle(self.screen, color, location, radius)
        pygame.display.flip()
        #print("Drew circle")
        return shape
    
    def draw_ellipse(self, color, width, height, x, y):
        shape = pygame.draw.ellipse(self.screen, color, pygame.Rect(width, height, height, width))
        shape.move(x, y)
        pygame.display.flip()
        #print("Drew ellipse")
        return shape
    
    def draw_line(self, color, width, start: pygame.Vector2, end: pygame.Vector2):
        shape = pygame.draw.line(self.screen, color, start, end, width)
        pygame.display.flip()
        #print("Drew line")
        return shape
    
    def draw_text(self, font_size, text, color, x, y):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(text, False, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.screen.blit(text, textRect)
        