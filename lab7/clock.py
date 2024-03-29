import pygame
import requests
from io import BytesIO

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Mouse Clock")

background_url = "https://i.pinimg.com/474x/6a/b9/1a/6ab91aafca1a5b62ea9b4f55ab04e1df.jpg"
response = requests.get(background_url)
background_image = pygame.image.load(BytesIO(response.content)).convert()

def load_image_from_url(url):
    response = requests.get(url)
    image = pygame.image.load(BytesIO(response.content)).convert_alpha()
    return image

mickey_seconds_hand = None

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = pygame.time.get_ticks()
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))

    second_angle = (current_time // 1000) % 60 * 6
    minute_angle = (current_time // 60000) % 60 * 6

    center_x, center_y = 300, 300
    second_hand_length = 200
    minute_hand_length = 180

    second_hand_end_x = center_x + second_hand_length * pygame.math.Vector2(1, 0).rotate(second_angle).x
    second_hand_end_y = center_y + second_hand_length * pygame.math.Vector2(1, 0).rotate(second_angle).y

    minute_hand_end_x = center_x + minute_hand_length * pygame.math.Vector2(1, 0).rotate(minute_angle).x
    minute_hand_end_y = center_y + minute_hand_length * pygame.math.Vector2(1, 0).rotate(minute_angle).y

    pygame.draw.line(screen, (255, 0, 0), (center_x/2, center_y/2), (second_hand_end_x/2, second_hand_end_y/2), 5)
    pygame.draw.line(screen, (0, 0, 255), (center_x/2, center_y/2), (minute_hand_end_x/2, minute_hand_end_y/2), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
