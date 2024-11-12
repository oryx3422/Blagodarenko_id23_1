import pygame
import random
import json
import os

def load_config():
    default_config = {
        "drop_density": 1.0,
        "min_speed": 2,
        "max_speed": 5,
        "min_angle": -1,
        "max_angle": 1
    }
    if not os.path.exists('config.json'):
        with open('config.json', 'w') as f:
            json.dump(default_config, f)
        return default_config
    with open('config.json', 'r') as f:
        return json.load(f)

class Drop:
    def __init__(self, x, y, speed, angle):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle

    def update(self):
        self.x += self.speed * self.angle / 100
        self.y += self.speed

def generate_drops(config, width, height):
    drops = []
    for _ in range(int(width * config['drop_density'])):
        x = random.randint(0, width)
        y = random.randint(-height, 0)
        speed = random.uniform(config['min_speed'], config['max_speed'])
        angle = random.uniform(config['min_angle'], config['max_angle'])
        drops.append(Drop(x, y, speed, angle))
    return drops

def main():
    pygame.init()

    config = load_config()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    drops = generate_drops(config, width, height)

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((230, 230, 255))

        for drop in drops:
            drop.update()
            if drop.y > height:
                drop.y = random.randint(-height, 0)
                drop.x = random.randint(0, width)
            pygame.draw.line(screen, (137, 48, 225), (drop.x, drop.y), (drop.x + drop.angle, drop.y + 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
