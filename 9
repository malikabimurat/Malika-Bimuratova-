import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Дополнительный слой, на котором будем хранить нарисованное
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # зальём белым фоном

clock = pygame.time.Clock()

# Цвета
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

current_color = colorRED  # Текущий цвет рисования

"""
Набор инструментов (modes):
 'line'  - простой «карандаш»
 'rect'  - прямоугольник
 'circle'- окружность
 'eraser'- ластик
 'square' - квадрат
 'rtriangle' - прямоугольный треугольник
 'triangle'  - равносторонний треугольник
 'rhombus'   - ромб
"""
mode = 'line'

drawing = False    # Флаг «ЛКМ зажата»
start_pos = (0, 0) # Точка, где нажали ЛКМ
thickness = 5      # Толщина линии/контура

# ------------------- ФУНКЦИИ РИСОВАНИЯ -------------------

def draw_line(surface, color, start, end, thickness):
    """Рисуем линию (карандаш) между start и end."""
    pygame.draw.line(surface, color, start, end, thickness)

def draw_rect(surface, color, start, end, thickness):
    """Рисуем прямоугольник, ограниченный точками start и end."""
    left = min(start[0], end[0])
    top = min(start[1], end[1])
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    rect = pygame.Rect(left, top, width, height)
    pygame.draw.rect(surface, color, rect, thickness)

def draw_square(surface, color, start, end, thickness):
    """
    Рисуем квадрат. Сторона = max по ширине/высоте
    bounding-box от start до end.
    """
    left = min(start[0], end[0])
    top = min(start[1], end[1])
    side = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(left, top, side, side)
    pygame.draw.rect(surface, color, rect, thickness)

def draw_circle(surface, color, start, end, thickness):
    """
    Рисуем окружность: 
     - Центр = середина отрезка (start, end)
     - Радиус = половина длины между start и end.
    """
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = int(math.dist(start, end) / 2)
    pygame.draw.circle(surface, color, (center_x, center_y), radius, thickness)

def draw_rtriangle(surface, color, start, end, thickness):
    """
    Рисуем прямоугольный треугольник.
    Чтобы «замкнуть» фигуру, используем 3 точки:
     A = start
     B = (start.x, end.y)
     C = end
    """
    (x1, y1) = start
    (x2, y2) = end
    # Точки (A, B, C) – 3 вершины треугольника
    A = (x1, y1)
    B = (x1, y2)
    C = (x2, y2)
    pygame.draw.polygon(surface, color, [A, B, C], thickness)

def draw_equilateral_triangle(surface, color, start, end, thickness):
    """
    Рисуем равносторонний треугольник, у которого отрезок (start -> end)
    является одной из сторон. Третья вершина вычисляется исходя
    из высоты h = (sqrt(3)/2)*side.
    """
    x1, y1 = start
    x2, y2 = end
    
    # Длина стороны:
    side = math.dist(start, end)
    
    # Центр отрезка (start -> end)
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    
    # Угол наклона отрезка (start->end)
    angle = math.atan2((y2 - y1), (x2 - x1))
    
    # Высота равностороннего треугольника
    height = side * (math.sqrt(3) / 2)
    
    # Координаты третьей вершины (x3, y3)
    # Двигаемся от середины перпендикулярно отрезку на расстояние height
    x3 = cx + height * math.cos(angle + math.pi / 2)
    y3 = cy + height * math.sin(angle + math.pi / 2)

    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)], thickness)

def draw_rhombus(surface, color, start, end, thickness):
    """
    Рисуем ромб, вписанный в bounding-box между start и end.
    """
    left = min(start[0], end[0])
    right = max(start[0], end[0])
    top = min(start[1], end[1])
    bottom = max(start[1], end[1])

    cx = (left + right) / 2
    cy = (top + bottom) / 2

    # Четыре вершины ромба
    top_point = (cx, top)
    right_point = (right, cy)
    bottom_point = (cx, bottom)
    left_point = (left, cy)

    points = [top_point, right_point, bottom_point, left_point]
    pygame.draw.polygon(surface, color, points, thickness)

def erase(surface, pos, size):
    """
    Ластик: рисуем белым квадратом в месте pos
    (Можно было бы сделать круглый ластик).
    """
    eraser_rect = pygame.Rect(pos[0] - size//2, pos[1] - size//2, size, size)
    pygame.draw.rect(surface, colorWHITE, eraser_rect)

# --------------------------------------------------------

running = True
while running:
    # Очищаем основной экран в белый, потом накладываем base_layer
    screen.fill(colorWHITE)
    screen.blit(base_layer, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --------- Обработка нажатий клавиш ----------
        if event.type == pygame.KEYDOWN:
            # Инструменты (смена mode):
            if event.key == pygame.K_1:
                mode = 'line'
            elif event.key == pygame.K_2:
                mode = 'rect'
            elif event.key == pygame.K_3:
                mode = 'circle'
            elif event.key == pygame.K_4:
                mode = 'eraser'
            elif event.key == pygame.K_5:
                mode = 'square'
            elif event.key == pygame.K_6:
                mode = 'rtriangle'
            elif event.key == pygame.K_7:
                mode = 'triangle'
            elif event.key == pygame.K_8:
                mode = 'rhombus'

            # Цвет
            if event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_g:
                current_color = colorGREEN
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_k:  # k -> black
                current_color = colorBLACK

            # Толщина кисти/контура
            if event.key == pygame.K_EQUALS:  # клавиша "="
                thickness += 1
            elif event.key == pygame.K_MINUS:
                thickness = max(1, thickness - 1)

        # --------- Нажатие ЛКМ ----------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка
                drawing = True
                start_pos = event.pos

        # --------- Отпускание ЛКМ ----------
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # По окончании рисования «финализируем» результат на base_layer
                if mode == 'rect':
                    draw_rect(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'circle':
                    draw_circle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'square':
                    draw_square(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'rtriangle':
                    draw_rtriangle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'triangle':
                    draw_equilateral_triangle(base_layer, current_color, start_pos, end_pos, thickness)
                elif mode == 'rhombus':
                    draw_rhombus(base_layer, current_color, start_pos, end_pos, thickness)
                # Если mode == 'line' или 'eraser', то рисовали «по ходу движения» 

        # --------- Движение мыши в зажатом состоянии ----------
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos

            if mode == 'line':
                # Рисуем сразу на base_layer, чтобы линии не исчезали 
                draw_line(base_layer, current_color, start_pos, current_pos, thickness)
                start_pos = current_pos
            elif mode == 'eraser':
                # Стираем небольшим квадратом
                erase(base_layer, current_pos, thickness * 2)

    # --------- «Предпросмотр» фигур (rect, circle, square, rtriangle, triangle, rhombus) ----------
    if drawing and mode in ('rect', 'circle', 'square', 'rtriangle', 'triangle', 'rhombus'):
        mouse_pos = pygame.mouse.get_pos()
        if mode == 'rect':
            draw_rect(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'circle':
            draw_circle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'square':
            draw_square(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'rtriangle':
            draw_rtriangle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'triangle':
            draw_equilateral_triangle(screen, current_color, start_pos, mouse_pos, thickness)
        elif mode == 'rhombus':
            draw_rhombus(screen, current_color, start_pos, mouse_pos, thickness)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
