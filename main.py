import pygame
pygame.init()
WIDTH = 500
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")
background = pygame.image.load("394383.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
pet = pygame.Rect(50, 50, 50, 50)
pet_speed = 2
foods = [pygame.Rect(120, 100, 25, 25),pygame.Rect(250, 180, 25, 25),pygame.Rect(400, 300, 25, 25)]
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pet.x -= pet_speed
    if keys[pygame.K_RIGHT]:
        pet.x += pet_speed
    if keys[pygame.K_UP]:
        pet.y -= pet_speed
    if keys[pygame.K_DOWN]:
        pet.y += pet_speed
    pet.x = max(0, min(pet.x, WIDTH - pet.width))
    pet.y = max(0, min(pet.y, HEIGHT - pet.height))
    for food in foods[:]:
        if pet.colliderect(food):
            foods.remove(food)
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 255), pet)
    for food in foods:
        pygame.draw.rect(screen, (255, 0, 0), food)
    if len(foods) == 0:
        text = font.render("Food Collected!", True, (255, 255, 255))
        x = (WIDTH - text.get_width()) // 2
        y = (HEIGHT - text.get_height()) // 2
        screen.blit(text, (x, y))
    pygame.display.update()
pygame.quit()