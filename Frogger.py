import pygame, random

pygame.init()
screen_width = 500
screen_height = 800
start_count, fake_frogs_list, winner = 0, [], False
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FROGGER")
menu_font = pygame.font.SysFont("comicsans", 40, True)
score_font = pygame.font.SysFont("comicsans", 30, True)
death_font = pygame.font.SysFont("comicsans", 60, True)

bg = pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\background.png")
bg = pygame.transform.scale(bg, (screen_width, screen_height))

frog_list_unsized = [pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\crop_1.png"),
                     pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\crop_2.png"),
                     pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\crop_3.png"),
                     pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\crop_4.png")]
frog_list = []
for image_unsized in frog_list_unsized:
    image = pygame.transform.scale(image_unsized, (50, 50))
    frog_list.append(image)


class Frog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.vel = 62
        self.direction_facing = "North"
        self.jump_cooldown = 0

    def rotate_frog(self, rotation):
        global frog_list, frog_list_unsized
        self.jump_cooldown += 1
        frog_list = []
        for image_unsized in frog_list_unsized:
            image = pygame.transform.scale(image_unsized, (50, 50))
            image = pygame.transform.rotate(image, rotation)
            frog_list.append(image)


class Car:  # REPRESENTS ALL OBJECTS (Not just cars)
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.width = 50

    def move_car_left(self, row, multiply=1):
        self.x -= (row.vel * multiply)

    def move_car_right(self, row, multiply=1):
        self.x += (row.vel * multiply)


def add_car(row, where):
    row.row_list.append(Car(row.y, where))
    row.newcar_count = 0


class Row:
    def __init__(self, y):
        self.y = y
        self.row_list = []
        self.newcar_count = random.choice(range(300, 500))
        self.vel = random.choice(range(4, 10))


def end_game(text):
    text_info_death = death_font.render(text, 1, (0, 0, 0))
    win.blit(text_info_death, (40, 150))
    pygame.display.update()
    pygame.time.wait(4000)


# --------------------------------------- ADDING OBJECTS IMAGES --------------------------------------- #
car_list_unsized = [pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\car1.png"),
                    pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\car2.png"),
                    pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\car3.png"),
                    pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\car4.png"),
                    pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\car5.png"),
                    pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\log.png")]
car_list_options = []
for image_unsized in car_list_unsized:
    image = pygame.transform.scale(image_unsized, (100, 50))
    car_list_options.append(image)

image = pygame.transform.scale(
    pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\lily_pad.png"), (50, 50))   # LILY-PAD ADDED SEPERATELY (As it is smaller size)
car_list_options.append(image)

# --------------------------------------- MENU --------------------------------------- #
text_info1 = menu_font.render('PRESS ANY KEY TO START!', 1, (0, 0, 0))
text_info2 = score_font.render('Try and get 3 frogs across', 1, (0, 0, 0))
text_info3 = score_font.render('in the quickest time', 1, (0, 0, 0))
gameInit = 0
while gameInit == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            gameInit = 1

    win.blit(bg, (0, 0))
    win.blit(text_info1, (40, 150))
    win.blit(text_info2, (50, 200))
    win.blit(text_info3, (50, 225))
    pygame.display.update()

# --------------------------------------- MAIN CODE --------------------------------------- #
frog = Frog(250, 745)
row1, row2, row3, row4, row5, row6, row7, row8, row9, row10 = Row(683), Row(621), Row(559), Row(497), Row(435), Row(
    308), Row(246), Row(184), Row(122), Row(60)
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    start_count += 1  # JUMP COOL-DOWN
    if frog.jump_cooldown >= 5:
        frog.jump_cooldown = 0
    elif frog.jump_cooldown > 0:
        frog.jump_cooldown += 1

    keys = pygame.key.get_pressed()  # FROG MOVEMENT + DIRECTION FACING
    if start_count >= 20:
        if keys[pygame.K_LEFT] and frog.jump_cooldown <= 0:
            frog.x -= frog.vel
            frog.direction_facing = "West"
            frog.rotate_frog(90)
        elif keys[pygame.K_RIGHT] and frog.jump_cooldown <= 0:
            frog.x += frog.vel
            frog.rotate_frog(270)
        elif keys[pygame.K_UP] and frog.y > frog.vel and frog.jump_cooldown <= 0:
            frog.y -= frog.vel
            frog.direction_facing = "North"
            frog.rotate_frog(0)
        elif keys[pygame.K_DOWN] and frog.y < (screen_height - frog.width - frog.vel) and frog.jump_cooldown <= 0:
            frog.y += frog.vel
            frog.rotate_frog(180)

    for row in [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]:  # BACKGROUND PROGRAM FOR OBJECTS
        row.newcar_count += row.vel
        if row == row1 or row == row3 or row == row5:
            if row.newcar_count >= 400:
                add_car(row, -100)
            for car in row.row_list:
                car.move_car_right(row)
                if car.x - 18 <= frog.x + 25 <= car.x + 125 and car.y - 25 <= frog.y + 25 <= car.y + 75:
                    run = False

        elif row == row2 or row == row4:
            if row.newcar_count >= 400:
                add_car(row, screen_width)
            for car in row.row_list:
                car.move_car_left(row)
                if car.x - 18 <= frog.x + 25 <= car.x + 125 and car.y - 25 <= frog.y + 25 <= car.y + 75:
                    run = False

        elif row == row6 or row == row8 or row == row10:
            if row.newcar_count >= (random.choice(range(150, 9000)) / (row.vel * 0.3)):
                add_car(row, -100)
            if row.row_list == []:
                could_run = False
            else:
                could_run = True
            for log in row.row_list:
                log.move_car_right(row, 0.8)
                if log.y - 25 <= frog.y + 25 <= log.y + 75 and log.x - 2 <= frog.x + 25 <= log.x + 100:
                    frog.x += (row.vel * 0.8)
                    could_run = False
                elif not log.y - 25 <= frog.y + 25 <= log.y + 75:
                    could_run = False
            if could_run:
                run = False

        elif row == row7 or row == row9:
            if row.newcar_count >= (random.choice(range(150, 9000)) / (row.vel * 0.3)):
                add_car(row, screen_width)
            if row.row_list == []:
                could_run = False
            else:
                could_run = True
            for log in row.row_list:
                log.move_car_left(row, 0.7)
                if log.y - 25 <= frog.y + 25 <= log.y + 75 and log.x - 2 <= frog.x + 25 <= log.x + 50:
                    frog.x -= (row.vel * 0.7)
                    could_run = False
                elif not log.y - 25 <= frog.y + 25 <= log.y + 75:
                    could_run = False
            if could_run:
                run = False

    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))

    i = 0
    for row in [row1, row2, row3, row4, row5]:  # TO BLIT ALL OBJECTS
        for car in row.row_list:
            win.blit(car_list_options[i], (car.x, car.y))
        i += 1

    for row in [row6, row7, row8, row9, row10]:
        for log in row.row_list:
            win.blit(car_list_options[i], (log.x, log.y))
        if i <= 5:
            i = 6
        else:
            i = 5

    if frog.x >= 470 or frog.x <= 0:  # LOSE IF PLAYER MOVES OUT OF SCREEN
        run = False

    if frog.jump_cooldown > 3:  # FOR THE FROGS AT END/TOP OF SCREEN (Get 3 = win)
        win.blit(frog_list[3], (frog.x, frog.y))
    else:
        win.blit(frog_list[frog.jump_cooldown], (frog.x, frog.y))

    if frog.y <= 30:
        fake_frogs_list.append([frog.x, frog.y])
        frog = Frog(250, 807)
    for froggy in fake_frogs_list:
        win.blit(pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load(r"C:\Users\nicho\PycharmProjects\pythonProject\PyGame Games\Froggo\Resources\crop_1.png"), (50, 50)), 180),
                 (froggy[0], froggy[1]))
        if len(fake_frogs_list) >= 3:
            winner = True

    text_info_death = score_font.render(('Time: ' + str(start_count // 10)), 1, (0, 0, 0))  # TO PRINT TIME
    win.blit(text_info_death, (10, 5))

    if not run:  # END THE GAME + TEXT
        end_game('YOU HAVE LOST')
    elif winner:
        end_game('YOU HAVE WON!!')
        run = False
    pygame.display.update()
pygame.quit()
