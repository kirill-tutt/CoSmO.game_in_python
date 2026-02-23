# <------ modules for work/модули для работы
import pygame
import random
import sys
# <------ abbreviation in code/сокращение в коде
watch = pygame.time.Clock()
rect_org = pygame.draw
# <------ working with the display/работа с дисплеем
pygame.init()
screen = pygame.display.set_mode((700, 1000))
pygame.display.set_caption('CoSmO')
icon = pygame.image.load('files/icon.png').convert_alpha()
pygame.display.set_icon(icon)
# <------ main menu with text/главное меню с текстом
menu_main_background = pygame.image.load('files/menu_fan.png').convert_alpha()
text_menu_main = pygame.font.Font('files/zubilo-black.otf', 140)
text_menu_main_render = text_menu_main.render('Cosmo', False, (194, 28, 255))
# <------ button with the text "Levels" in the main menu/кнопка с текстом уровни в главном меню
text_menu_main_start = pygame.font.Font('files/Шрифт Майнкрафт.ttf', 70)
text_menu_main_start_render = text_menu_main_start.render('Старт', False, (201, 54, 54))
# <------ the sound of a stone exploding against a shell/звук взрыва камня об снарядов
explosion_of_sound_main = [
    pygame.mixer.Sound('files/370b925a30aca01.mp3'),
    pygame.mixer.Sound('files/c0647023ca0a00c.mp3'),
    pygame.mixer.Sound('files/zvuk-petardy.mp3'),
    pygame.mixer.Sound('files/big-bang.mp3')
]
# <------ background/задний фон
background = pygame.image.load('files/space-galaxy-background.jpg').convert_alpha()
# <------ arrow to exit to the menu/стрелка для выхода в меню
text_menu = pygame.font.Font('files/Шрифт Майнкрафт.ttf', 35)
text_restart_menu = text_menu.render('меню', False, (138, 242, 168))
# <------ player/игрок
player_ran = pygame.image.load('player/player_1.png').convert_alpha()
player_x = 280
player_y = 850
player_speed_level_max = 8
player_speed = 5
player_speed_main = 5
player_speed_stop = 0
# <------ cartridge/патрон
bullet = pygame.image.load('files/free-icon-bullet-2218066.png').convert_alpha()
bullets = []
bullet_speed = 7
# <------ music/музыка
bg_music = pygame.mixer.Sound('files/kosmos-28439.mp3')
bg_bullet = pygame.mixer.Sound('files/laser-blast-descend_gy7c5deo.mp3')
bg_loss = pygame.mixer.Sound('files/oglushitelnyiy-blizkiy-vzryiv.mp3')
bg_music.play()
m = 0
mm = 0
# <------ numbers for the level/цифры для уровня
numbers = [
    pygame.image.load('numbers/number_1.png').convert_alpha(),
    pygame.image.load('numbers/number_2.png').convert_alpha(),
    pygame.image.load('numbers/number_3.png').convert_alpha(),
    pygame.image.load('numbers/number_4.png').convert_alpha(),
    pygame.image.load('numbers/number_5.png').convert_alpha(),
    pygame.image.load('numbers/number_6.png').convert_alpha(),
    pygame.image.load('numbers/number_7.png').convert_alpha(),
    pygame.image.load('numbers/number_8.png').convert_alpha(),
    pygame.image.load('numbers/number_9.png').convert_alpha(),
    pygame.image.load('numbers/number_10.png').convert_alpha()
]
left_arrow = pygame.image.load('files/стрелка_влево.png').convert_alpha()
# <------ enemy/враг
stone = pygame.image.load('files/stone.png').convert_alpha()
stone_enemy_0 = []
stone_enemy_1 = []
stone_enemy_2 = []
stone_enemy_3 = []
stone_enemy_4 = []
stone_y = -200
stone_speed_stop = 0
stone_speed_level_1 = 1
stone_speed_level_2 = 2
stone_speed_level_3 = 3
stone_speed_level_4 = 4
stone_speed_level_5 = 5
# <------ ship explosion at death/взрыв корабля при смерти
boom_player = pygame.image.load('boom_player/explosion_1.png').convert_alpha()
boom_walk = [
    pygame.image.load('boom_player/explosion_1.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_2.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_3.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_4.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_5.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_6.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_7.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_8.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_9.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_10.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_11.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_12.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_13.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_14.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_15.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_16.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_17.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_18.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_19.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_20.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_21.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_22.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_23.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_24.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_25.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_26.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_27.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_28.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_29.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_30.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_31.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_32.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_33.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_34.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_35.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_36.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_37.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_38.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_38.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_39.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_40.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_41.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_42.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_43.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_44.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_45.png').convert_alpha(),
    pygame.image.load('boom_player/explosion_46.png').convert_alpha(),
]
boom_count = 0
# <------ Import textures from the settings menu/импорт текстур с меню настроек
setting_stop = pygame.image.load('files/free-icon-pause-11450250 (2).png').convert_alpha()
setting_play = pygame.image.load('files/free-icon-end-9403126.png').convert_alpha()
# <------ Importing text and cross textures/импорт текстуры текстов и крестика
level_text_5 = pygame.image.load('files/Надпись для уровня 5.png')
level_text_6 = pygame.image.load('files/Надпись для уровня 6.png')
cross_level_text = pygame.image.load('files/free-icon-cross-mark-4225690.png')
# <------ check/счет
check = pygame.font.Font(None, 75)
check_text = check.render('счет', False, (134, 94, 242))
# <------ working with the loss screen/работа с экраном проигрыша
text = pygame.font.Font('files/Шрифт Майнкрафт.ttf', 35)
text_load = text.render('Проигрыш, ваш счёт:', False, (242, 33, 71))
text_restart = text.render('Играть снова', False, (242, 33, 71))
# <------ timer for the enemy/таймер для врага
stone_timer = pygame.USEREVENT + 1
pygame.time.set_timer(stone_timer, 1000)
# <------ beginning of the cycle/начало цикла
level_1 = 0
level_2 = 0
level_3 = 0
level_4 = 0
level_5_1 = 0
level_5_2 = 0
level_6_1 = 0
level_6_2 = 0
menu_level = 0
menu_main = 1
running = True
# <------ Assigning keys on the keyboard, changing buttons/назначение клавиш на клавиатуре изменения кнопок
key_SPACE = pygame.K_SPACE
# <------ score/счёт очков
chet = 0
while running:
    # <------ mouse and keyboard/мышка и клавиатура
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    # <------ Setting up and rendering the game's main menu/настройка и отрисовка главного меню игры
    if menu_main == 1:
        screen.blit(menu_main_background, (0, 0))
        screen.blit(text_menu_main_render, (150, 10))
        menu_start_2 = rect_org.rect(screen, (23, 90, 191), pygame.Rect((150, 535), (420, 150)))
        menu_start_1 = rect_org.rect(screen, (91, 151, 240), pygame.Rect((160, 545), (400, 125)))
        screen.blit(text_menu_main_start_render, (190, 550))
        if menu_start_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт меню уровней')
            menu_main = 0
            menu_level = 1
    # <------ Setting up and rendering the main menu of levels/настройка и отрисовка главного меню уровней
    if menu_level == 1:
        screen.fill((39, 214, 182))
        # <------ drawing a square around the numbers/отрисовка квадрата вокруг цифр
            # <------ first row of the menu/первый ряд меню
        numbers_1_rect = numbers[0].get_rect(topleft=(40, 200))
        numbers_2_rect = numbers[1].get_rect(topleft=(210, 200))
        numbers_3_rect = numbers[2].get_rect(topleft=(372, 200))
        numbers_4_rect = numbers[3].get_rect(topleft=(532, 200))
            # <------ second row of the menu/второй ряд меню
        numbers_5_rect = numbers[4].get_rect(topleft=(210, 375))
        numbers_6_rect = numbers[5].get_rect(topleft=(372, 375))
        # <------ rendering the texture of numbers/отрисовка текстуры цифр
            # <------ first row of the menu/первый ряд меню
        screen.blit(numbers[0], (40, 200))
        screen.blit(numbers[1], (210, 200))
        screen.blit(numbers[2], (372, 200))
        screen.blit(numbers[3], (532, 200))
            # <------ second row of the menu/второй ряд меню
        screen.blit(numbers[4], (210, 375))
        screen.blit(numbers[5], (372, 375))
        # <------ drawing the texture of the arrow and the square next to it/отрисовка текстуры стрелки и квадрата возле неё
        screen.blit(left_arrow, (290, 700))
        left_arrow_rect = left_arrow.get_rect(topleft=(290, 700))
        # <------ Checking whether the left arrow key was pressed/проверка нажатия мышки на стрелку влево
        if left_arrow_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu_level = 0
            menu_main = 1
        # <------ checking mouse clicks on a level/проверка нажатия мышки на уровень
        if numbers_1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт первого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            level_1 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт второго уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            level_2 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт третьего уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            level_3 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_4_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт четвёртого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            level_4 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_5_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт пятого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            level_5_1 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
        if numbers_6_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            print('Старт шестого уровня')
            player_x = 280
            player_y = 850
            menu_level = 0
            level_6_1 = 1
            stone_enemy_0.clear()
            stone_enemy_1.clear()
            stone_enemy_2.clear()
            stone_enemy_3.clear()
            stone_enemy_4.clear()
    # <------ we set a random value for the stone on the X axis/задаем рандомное значение для камня на оси X
    stone_enemy_0_1 = random.randrange(25,600)
    stone_enemy_0_2 = random.randrange(25, 600)
    stone_enemy_0_3 = random.randrange(25,600)
    stone_enemy_0_4 = random.randrange(25,600)
    stone_enemy_0_5 = random.randrange(25,600)
    # <------ draw a square around the stone/отрисовываем квадрат вокруг камня
    stone_rect_0_1 = stone.get_rect(topleft=(stone_enemy_0_1, stone_y))
    stone_rect_0_2 = stone.get_rect(topleft=(stone_enemy_0_2, stone_y))
    stone_rect_0_3 = stone.get_rect(topleft=(stone_enemy_0_3, stone_y))
    stone_rect_0_4 = stone.get_rect(topleft=(stone_enemy_0_4, stone_y))
    stone_rect_0_5 = stone.get_rect(topleft=(stone_enemy_0_5, stone_y))
    # <------ draw a square around the player and the cartridge/отрисовываем квадрат вокруг игрока и патрона
    player_rect = player_ran.get_rect(topleft=(player_x, player_y))
    bullet_rect = bullet.get_rect(topleft=(player_x, player_y))
    # <------ we draw a square around the cross from the text at the level/отрисовываем квадрат вокруг крестика из текста на уровне
    cross_level_text_rect = cross_level_text.get_rect(topleft=(565, 273))
    # <------ Draw a square for my settings/отрисовываем квадрат для меня настроек
    setting_rect_1 = setting_stop.get_rect(topleft=(660, 10))
    setting_rect_2 = setting_play.get_rect(topleft=(662, 50))
    # <------ draw a square for the text during playback/отрисовываем квадрат для текста во время проигрыша
    text_restart_rect = text_restart.get_rect(topleft=(150, 450))
    text_restart_menu_rect = text_restart_menu.get_rect(topleft=(270, 800))
    # <------ function to play explosion sound/функция для воспроизведения звук взрыва
    def explosion_of_sound():
        explosion_of_sound_main[random.randrange(0, 3+1)].play()
    # <------ working on the first level/работа над первым уровнем
    if level_1 == 1:
        #  <------ We check hovering the mouse over the settings square - it works for all levels/проверяем наведение мышки на квадрат настроек - работает для всех уровней
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_1 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y < -50:
                        stone_enemy_0.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_1 = 1
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ the beginning of everything for the level/начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_1

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    level_1 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)
                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                            explosion_of_sound()
    if level_1 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level_1 = 0
            level_2 = 0
            level_3 = 0
            level_4 = 0
            level_5_1 = 0
            level_5_2 = 0
            level_6_1 = 0
            level_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            boom_count = 0
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            level_1 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE

        # <------ работа над вторым уровнем
    # <------ working on the second level/работа над вторым уровнем
    if level_2 == 1:
        #  <------ проверяем наведение мышки на квадрат настроек - работает для всех уровней
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_2 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y < -50:
                        stone_enemy_0.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_2 = 2
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_2

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    level_2 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_2

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    level_2 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                            explosion_of_sound()
    if level_2 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level_1 = 0
            level_2 = 0
            level_3 = 0
            level_4 = 0
            level_5_1 = 0
            level_5_2 = 0
            level_6_1 = 0
            level_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            boom_count = 0
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            level_2 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE  
    # <------ работа над третьим уровнем
    # <------ working on the third level/работа над третьим уровнем
    if level_3 == 1:
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_3 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y < -50:
                        stone_enemy_0.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_3 = 3
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_3

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    level_3 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_3

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    level_3 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_3

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    level_3 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                            explosion_of_sound()
    if level_3 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level_1 = 0
            level_2 = 0
            level_3 = 0
            level_4 = 0
            level_5_1 = 0
            level_5_2 = 0
            level_6_1 = 0
            level_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            level_3 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ working on the fourth level/работа над четвертым уровнем
    if level_4 == 1:
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_4 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_0.pop(i)

                    if player_rect.colliderect(el):
                        level_4 = 2
            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_1.pop(i)

                    if player_rect.colliderect(el):
                        level_4 = 2
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_2.pop(i)

                    if player_rect.colliderect(el):
                        level_4 = 2
            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_4

                    if el.y > 1500:
                        stone_enemy_3.pop(i)

                    if player_rect.colliderect(el):
                        level_4 = 2
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_4 = 4
            bullet_speed = 7
            if m == 0:
                bg_music.play(loops=0)
                m = 1

        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))

        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    level_4 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    level_4 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    level_4 = 2
        if stone_enemy_3:
            for (i, el) in enumerate(stone_enemy_3):
                screen.blit(stone, el)
                el.y += stone_speed_level_4

                if el.y > 1500:
                    stone_enemy_3.pop(i)

                if player_rect.colliderect(el):
                    level_4 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_3:
                    for (index, ghost_el) in enumerate(stone_enemy_3):
                        if el.colliderect(ghost_el):
                            stone_enemy_3.pop(index)
                            chet += 1
                            explosion_of_sound()
    if level_4 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        stone_enemy_3.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level_1 = 0
            level_2 = 0
            level_3 = 0
            level_4 = 0
            level_5_1 = 0
            level_5_2 = 0
            level_6_1 = 0
            level_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            level_4 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ work on the fifth level/работа над пятым уровнем
    if level_5_1 == 1:
        player_speed_main = player_speed_stop
        stone_speed_level_5 = stone_speed_stop
        m = 0
        key_SPACE = 0
        bullet_speed = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        screen.blit(level_text_5, (100, 270))
        screen.blit(cross_level_text, (565, 273))
        if cross_level_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    if el.y > 1500:
                        stone_enemy_1.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_2.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    if el.y > 1500:
                        stone_enemy_4.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_5 = 7
            bullet_speed = 7
            level_5_2 = 1
            level_5_1 = 0
    if level_5_2 == 1:
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        watch.tick(60)
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_5 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_0.pop(i)

            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_1.pop(i)

            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_2.pop(i)

            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_5

                    if el.y > 1500:
                        stone_enemy_4.pop(i)
        if m == 0:
            bg_music.play(loops=0)
            m = 1
        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    level_5_2 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    level_5_2 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    level_5_2 = 2
        if stone_enemy_3:
            for (i, el) in enumerate(stone_enemy_3):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_3.pop(i)

                if player_rect.colliderect(el):
                    level_5_2 = 2
        if stone_enemy_4:
            for (i, el) in enumerate(stone_enemy_4):
                screen.blit(stone, el)
                el.y += stone_speed_level_5

                if el.y > 1500:
                    stone_enemy_4.pop(i)

                if player_rect.colliderect(el):
                    level_5_2 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_3:
                    for (index, ghost_el) in enumerate(stone_enemy_3):
                        if el.colliderect(ghost_el):
                            stone_enemy_3.pop(index)
                            chet += 1
                            explosion_of_sound()
                if stone_enemy_4:
                    for (index, ghost_el) in enumerate(stone_enemy_4):
                        if el.colliderect(ghost_el):
                            stone_enemy_4.pop(index)
                            chet += 1
                            explosion_of_sound()
    if level_5_2 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        stone_enemy_3.clear()
        stone_enemy_4.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level_1 = 0
            level_2 = 0
            level_3 = 0
            level_4 = 0
            level_5_1 = 0
            level_5_2 = 0
            level_6_1 = 0
            level_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            level_5_2 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ working on the sixth level/работа над шестым уровнем
    if level_6_1 == 1:
        player_speed_main = player_speed_stop
        stone_speed_level_6 = stone_speed_stop
        m = 0
        key_SPACE = 0
        bullet_speed = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        screen.blit(level_text_6, (100, 270))
        screen.blit(cross_level_text, (565, 273))
        if cross_level_text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    if el.y > 1500:
                        stone_enemy_1.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_2.pop(i)
            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    if el.y > 1500:
                        stone_enemy_0.pop(i)
            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    if el.y > 1500:
                        stone_enemy_4.pop(i)
            key_SPACE = pygame.K_SPACE
            player_speed_main = player_speed
            stone_speed_level_6 = 7
            bullet_speed = 7
            level_6_2 = 1
            level_6_1 = 0
    if level_6_2 == 1:
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(player_ran, (player_x, player_y))
        watch.tick(45)
        if setting_rect_1.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            bg_music.stop()
            player_speed_main = player_speed_stop
            stone_speed_level_5 = stone_speed_stop
            m = 0
            key_SPACE = 0
            bullet_speed = 0
        if setting_rect_2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if stone_enemy_0:
                for (i, el) in enumerate(stone_enemy_0):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_0.pop(i)

            if stone_enemy_1:
                for (i, el) in enumerate(stone_enemy_1):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_1.pop(i)

            if stone_enemy_2:
                for (i, el) in enumerate(stone_enemy_2):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_2.pop(i)

            if stone_enemy_3:
                for (i, el) in enumerate(stone_enemy_3):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_3.pop(i)
            if stone_enemy_4:
                for (i, el) in enumerate(stone_enemy_4):
                    screen.blit(stone, el)
                    el.y += stone_speed_level_6

                    if el.y > 1500:
                        stone_enemy_4.pop(i)
        if m == 0:
            bg_music.play(loops=0)
            m = 1
        text_cheat = text.render(f"{chet}", True, (242, 33, 71))
        text_rect = text_cheat.get_rect(center=(350, 50))
        screen.blit(text_cheat, text_rect)
        #  <------ начало всего для уровня
        if stone_enemy_0:
            for (i, el) in enumerate(stone_enemy_0):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_0.pop(i)

                if player_rect.colliderect(el):
                    level_6_2 = 2
        if stone_enemy_1:
            for (i, el) in enumerate(stone_enemy_1):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_1.pop(i)

                if player_rect.colliderect(el):
                    level_6_2 = 2
        if stone_enemy_2:
            for (i, el) in enumerate(stone_enemy_2):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_2.pop(i)

                if player_rect.colliderect(el):
                    level_6_2 = 2
        if stone_enemy_3:
            for (i, el) in enumerate(stone_enemy_3):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_3.pop(i)

                if player_rect.colliderect(el):
                    level_6_2 = 2
        if stone_enemy_4:
            for (i, el) in enumerate(stone_enemy_4):
                screen.blit(stone, el)
                el.y += stone_speed_level_6

                if el.y > 1500:
                    stone_enemy_4.pop(i)

                if player_rect.colliderect(el):
                    level_6_2 = 2
        if bullets:
            for el in bullets:
                screen.blit(bullet, (el.x, el.y))
                el.y -= bullet_speed

                if el.y < -50:
                    bullets.pop(0)

                if stone_enemy_0:
                    for (index, ghost_el) in enumerate(stone_enemy_0):
                        if el.colliderect(ghost_el):
                            stone_enemy_0.pop(index)
                            chet += 1
                if stone_enemy_1:
                    for (index, ghost_el) in enumerate(stone_enemy_1):
                        if el.colliderect(ghost_el):
                            stone_enemy_1.pop(index)
                            chet += 1
                if stone_enemy_2:
                    for (index, ghost_el) in enumerate(stone_enemy_2):
                        if el.colliderect(ghost_el):
                            stone_enemy_2.pop(index)
                            chet += 1
                if stone_enemy_3:
                    for (index, ghost_el) in enumerate(stone_enemy_3):
                        if el.colliderect(ghost_el):
                            stone_enemy_3.pop(index)
                            chet += 1
                if stone_enemy_4:
                    for (index, ghost_el) in enumerate(stone_enemy_4):
                        if el.colliderect(ghost_el):
                            stone_enemy_4.pop(index)
                            chet += 1
    if level_6_2 == 2:
        bg_music.stop()
        stone_enemy_0.clear()
        stone_enemy_1.clear()
        stone_enemy_2.clear()
        stone_enemy_3.clear()
        stone_enemy_4.clear()
        bullets.clear()
        player_speed_main = player_speed_stop
        key_SPACE = 0
        screen.blit(background, (0, 0))
        screen.blit(setting_stop, (660, 10))
        screen.blit(setting_play, (662, 50))
        screen.blit(boom_walk[boom_count], (player_x - 90, player_y - 75))
        if boom_count == 46:
            pass
        else:
            boom_count += 1
        if mm == 0:
            bg_loss.play(loops=0)
            mm = 1
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((120, 418), (460, 110)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((130, 429), (440, 90)))
        screen.blit(text_load, (50, 180))
        rect_org.rect(screen, (255, 255, 255), pygame.Rect((240, 795), (220, 75)))
        rect_org.rect(screen, (0, 204, 34), pygame.Rect((245, 800), (210, 65)))
        screen.blit(text_restart_menu, (270, 800))
        text_cheat = text.render(f"{chet}", False, (242, 33, 71))
        text_rect_2 = text_cheat.get_rect(center=(350, 290))
        screen.blit(text_cheat, text_rect_2)
        screen.blit(text_restart, text_restart_rect)

        if text_restart_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            level_1 = 0
            level_2 = 0
            level_3 = 0
            level_4 = 0
            level_5_1 = 0
            level_5_2 = 0
            level_6_1 = 0
            level_6_2 = 0
            menu_level = 0
            menu_main = 1
            player_speed_main = player_speed
            bg_music.play(loops=0)
            m = 0
            mm = 0
            chet = 0
            boom_count = 0
            key_SPACE = pygame.K_SPACE
        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            player_x = 280
            player_y = 850
            level_6_2 = 1
            bg_music.play()
            boom_count = 0
            player_speed_main = player_speed
            m = 0
            mm = 0
            chet = 0
            key_SPACE = pygame.K_SPACE
    # <------ moving right and left/перемещение вправо и влево
    if keys[pygame.K_LEFT] and player_x > 25:
        player_x -= player_speed_main
    elif keys[pygame.K_RIGHT] and player_x < 600:
        player_x += player_speed_main
    elif keys[pygame.K_a] and player_x > 25:
        player_x -= player_speed_main
    elif keys[pygame.K_d] and player_x < 600:
        player_x += player_speed_main
    # <------ up and down movement; movement limitation/перемещение вверх и вниз; ограничение по перемещению
    if keys[pygame.K_UP]  and player_y > 30:
        player_y -= player_speed_main
    elif keys[pygame.K_DOWN] and player_y < 860:
        player_y += player_speed_main
    elif keys[pygame.K_w] and player_y > 30:
        player_y -= player_speed_main
    elif keys[pygame.K_s] and player_y < 860:
        player_y += player_speed_main
# <------ cycle for buttons and events/цикл для кнопок и событий
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            sys.exit(0)
        if event.type == stone_timer:
            stone_enemy_0.append(stone.get_rect(topleft=(stone_enemy_0_1, stone_y)))
            stone_enemy_1.append(stone.get_rect(topleft=(stone_enemy_0_2, stone_y)))
            stone_enemy_2.append(stone.get_rect(topleft=(stone_enemy_0_3, stone_y)))
            stone_enemy_3.append(stone.get_rect(topleft=(stone_enemy_0_4, stone_y)))
            stone_enemy_4.append(stone.get_rect(topleft=(stone_enemy_0_5, stone_y)))
        if (level_1 or level_2 or level_3 or level_4 or level_5_2 or level_6_2) and event.type == pygame.KEYUP and event.key == key_SPACE:
            bullets.append(bullet.get_rect(topleft=(player_x, player_y - 30)))
            bg_bullet.play()
    pygame.display.update()
    watch.tick(120)
