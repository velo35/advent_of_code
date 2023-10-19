import pygame
import day_22

def blit_map(map_surface, scale, offset_x, offset_y):
    scaled_map = pygame.transform.scale_by(map_surface, scale)    
    screen.blit(scaled_map, (content_offset_x, content_offset_y))

def draw_commands():
    font_size = 24
    font = pygame.font.SysFont('andalemono', font_size)
    mid_x = screen_width // 2
    width = 0
    if command_ndx > 0:
        text_surface = font.render(' '.join([str(x) for x in commands[:command_ndx]]) + ' ', False, 'gray')
        screen.blit(text_surface, (mid_x - text_surface.get_width(), screen_height - text_surface.get_height() - 10))
        width = text_surface.get_width()

    text_surface = font.render(' '.join([str(x) for x in commands[command_ndx:]]), False, 'white')
    screen.blit(text_surface, (mid_x, screen_height - text_surface.get_height() - 10))

def step_command(ins, x, y, dir, map, d_map):
    for i in range(ins):
        d_map[y][x] = d_dir[dir.value]
        next_x, next_y, next_dir = day_22.next_step_sample(x, y, dir) if use_sample else day_22.next_step_real(x, y, dir)
        if map[next_y][next_x] == '#':
            break
        x = next_x
        y = next_y
        dir = next_dir

    return x, y, dir

def render_map(map, color):
    font_size = 24
    font = pygame.font.SysFont('andalemono', font_size)
    line_surfaces = [font.render(''.join(line), False, color) for line in map]
    surface_width = line_surfaces[0].get_width()
    surface_height = sum([line_surface.get_height() for line_surface in line_surfaces])
    map_surface = pygame.Surface((surface_width, surface_height), pygame.SRCALPHA)
    for i, line_surface in enumerate(line_surfaces):
        map_surface.blit(line_surface, (0, i * line_surfaces[0].get_height()))

    return map_surface

if __name__ == '__main__':
    use_sample = False
    map, commands = day_22.init(use_sample)

    d_map = [[' '] * len(line) for line in map]
    d_dir = ['>', 'v', '<', '^']

    Direction = day_22.Direction
    x, y = map[0].find('.'), 0
    dir = Direction.Right

    d_map[y][x] = d_dir[dir.value]

    screen_width = 1280
    screen_height = 720

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    map_surface = render_map(map, 'white')
    d_map_surface = render_map(d_map, 'magenta')

    content_width = map_surface.get_width()
    content_height = map_surface.get_height()

    min_scale = min(1.0, (screen_height - 100) / content_height, (screen_width - 100) / content_width)
    scale = min_scale

    content_offset_x = (screen_width - scale * content_width) / 2
    content_offset_y = (screen_height - scale * content_height) / 2

    command_ndx = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                if command_ndx < len(commands):
                    ins = commands[command_ndx]
                    if isinstance(ins, int):
                        x, y, dir = step_command(ins, x, y, dir, map, d_map)
                    else:
                        dir = dir.turn(ins)
                    command_ndx += 1
                    d_map[y][x] = d_dir[dir.value]
                    d_map_surface = render_map(d_map, 'magenta')
                else:
                    print('no commands left!')

        d_scale = pygame.key.get_pressed()[pygame.K_t] - pygame.key.get_pressed()[pygame.K_r]
        if d_scale:
            d_scale *= 0.01
            content_offset_x -= d_scale * (screen_width / 2 - content_offset_x) / scale
            content_offset_y -= d_scale * (screen_height / 2 - content_offset_y) / scale
            scale += d_scale

        pan_horizontal = pygame.key.get_pressed()[pygame.K_LEFT] - pygame.key.get_pressed()[pygame.K_RIGHT]
        content_offset_x += pan_horizontal * 8

        pan_vertical = pygame.key.get_pressed()[pygame.K_UP] - pygame.key.get_pressed()[pygame.K_DOWN]
        content_offset_y += pan_vertical * 8

        screen.fill('black')
        blit_map(map_surface, scale, content_offset_x, content_offset_y)
        blit_map(d_map_surface, scale, content_offset_x, content_offset_y)
        draw_commands()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()