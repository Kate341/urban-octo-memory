import pygame
import math

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Paint & Shape Drawing")
CLOCK = pygame.time.Clock()

# Creating of paint's canvas
canvas = pygame.Surface(screen.get_size())
canvas.fill((255, 255, 255))

# Load and resize images to be consistent in size
def load_and_resize_image(image_path, size=(40, 40)):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)

# Implementing resize
image_rectangle = load_and_resize_image("/home/kali/my_project/urban-octo-memory/Lab9/rectangle.png")
image_circle = load_and_resize_image("/home/kali/my_project/urban-octo-memory/Lab9/circle.png")
image_square = load_and_resize_image("/home/kali/my_project/urban-octo-memory/Lab9/square.png")
image_triangle = load_and_resize_image("/home/kali/my_project/urban-octo-memory/Lab9/triangle.png")
image_equilateral_triangle = load_and_resize_image("/home/kali/my_project/urban-octo-memory/Lab9/eq_triangle.png")
image_rhombus = load_and_resize_image("/home/kali/my_project/urban-octo-memory/Lab9/rhombus.png")

# Getting rectangles of images
rectangle_rect = image_rectangle.get_rect(topleft=(10, 10))
circle_rect = image_circle.get_rect(topleft=(rectangle_rect.right + 10, 10))
square_rect = image_square.get_rect(topleft=(circle_rect.right + 10, 10))
triangle_rect = image_triangle.get_rect(topleft=(square_rect.right + 10, 10))
equilateral_triangle_rect = image_equilateral_triangle.get_rect(topleft=(triangle_rect.right + 10, 10))
rhombus_rect = image_rhombus.get_rect(topleft=(equilateral_triangle_rect.right + 10, 10))

# Colors
color_palette = [
    (0, 0, 0),       # Black
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 165, 0),   # Orange
    (255, 255, 255), # White
]

palette_rects = []
for i, color in enumerate(color_palette):
    rect = pygame.Rect(10 + i * 40, 60, 30, 30)  # Positions of color blocks
    palette_rects.append((rect, color))

running = True
color_brush = (0, 0, 0)
brush_size = 10
prev_pos = None

# Chosen instruments: "brush", "rectangle", "circle", "square", "triangle", "equilateral_triangle", "rhombus", "eraser"
current_tool = "brush"
drawing = False
start_pos = None

# eq_triangle_functions
def draw_equilateral_triangle(surface, color, top_left, side_length):
    height = (math.sqrt(3) / 2) * side_length
    points = [
        top_left,
        (top_left[0] + side_length // 2, top_left[1] - height),
        (top_left[0] + side_length, top_left[1])
    ]
    pygame.draw.polygon(surface, color, points, 2)

# rhombus_function
def draw_rhombus(surface, color, top_left, width, height):
    points = [
        top_left,
        (top_left[0] + width // 2, top_left[1] - height // 2),
        (top_left[0] + width, top_left[1]),
        (top_left[0] + width // 2, top_left[1] + height // 2)
    ]
    pygame.draw.polygon(surface, color, points, 2)

#Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            #Figures logic
            if rectangle_rect.collidepoint(pos):
                current_tool = "rectangle"
            elif circle_rect.collidepoint(pos):
                current_tool = "circle"
            elif square_rect.collidepoint(pos):
                current_tool = "square"
            elif triangle_rect.collidepoint(pos):
                current_tool = "triangle"
            elif equilateral_triangle_rect.collidepoint(pos):
                current_tool = "equilateral_triangle"
            elif rhombus_rect.collidepoint(pos):
                current_tool = "rhombus"
            elif current_tool in ["rectangle", "circle", "square", "triangle", "equilateral_triangle", "rhombus"]:
                start_pos = pos
                drawing = True
            for rect, color in palette_rects: # Check if a color is selected
                if rect.collidepoint(pos):
                    color_brush = color

        if pygame.mouse.get_pressed()[0] and current_tool in ["brush", "eraser"]: #Main drawing(start)
            pos = pygame.mouse.get_pos()
            if not (rectangle_rect.collidepoint(pos) or circle_rect.collidepoint(pos)):
                color = (255, 255, 255) if current_tool == "eraser" else color_brush
                if prev_pos is not None:
                    pygame.draw.line(canvas, color, prev_pos, pos, brush_size * 2)
                prev_pos = pos
        else:
            prev_pos = None

        if event.type == pygame.MOUSEBUTTONUP and drawing: #Main drawing(end)
            end_pos = event.pos
            if start_pos and end_pos:
                x1, y1 = start_pos
                x2, y2 = end_pos
                width = abs(x2 - x1)
                height = abs(y2 - y1)
                top_left = (min(x1, x2), min(y1, y2))

                if current_tool == "rectangle": # If figures were chosen
                    pygame.draw.rect(canvas, color_brush, (*top_left, width, height), 2)
                elif current_tool == "circle":
                    radius = max(width, height) // 2
                    center = (x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2)
                    pygame.draw.circle(canvas, color_brush, center, radius, 2)
                elif current_tool == "square":
                    side = min(width, height)
                    pygame.draw.rect(canvas, color_brush, (*top_left, side, side), 2)
                elif current_tool == "triangle":
                    pygame.draw.polygon(canvas, color_brush, [top_left, (x2, y2), (x1, y2)], 2)
                elif current_tool == "equilateral_triangle":
                    draw_equilateral_triangle(canvas, color_brush, top_left, width)
                elif current_tool == "rhombus":
                    draw_rhombus(canvas, color_brush, top_left, width, height)

            drawing = False
            start_pos = None

        if event.type == pygame.KEYDOWN: #Colors and main instruments logic
            if event.key == pygame.K_b:
                current_tool = "brush"
            elif event.key == pygame.K_e:
                current_tool = "eraser"
            elif event.key == pygame.K_1:
                color_brush = (0, 0, 0)       # Black
            elif event.key == pygame.K_2:
                color_brush = (0, 255, 0)     # Green
            elif event.key == pygame.K_3:
                color_brush = (0, 0, 255)     # Blue
            elif event.key == pygame.K_4:
                color_brush = (255, 0, 0)     # Red
            elif event.key == pygame.K_5:
                color_brush = (255, 255, 0)   # Yellow

    # Showing canvas
    screen.blit(canvas, (0, 0))

    # Showing figures' buttons
    screen.blit(image_rectangle, rectangle_rect)
    screen.blit(image_circle, circle_rect)
    screen.blit(image_square, square_rect)
    screen.blit(image_triangle, triangle_rect)
    screen.blit(image_equilateral_triangle, equilateral_triangle_rect)
    screen.blit(image_rhombus, rhombus_rect)

    # Showing colors' buttons
    for rect, color in palette_rects:
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()