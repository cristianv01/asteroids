from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", pygame.Vector2(self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            newradius = self.radius - ASTEROID_MIN_RADIUS
            newAsteroid1 = Asteroid(self.position.x, self.position.y, newradius)
            newAsteroid2 = Asteroid(self.position.x, self.position.y, newradius)

            newAsteroid1.velocity = vec1 * 1.2
            newAsteroid2.velocity = vec2 * 1.2

