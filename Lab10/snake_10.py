
import psycopg2


# Подключение к БД
conn = psycopg2.connect(
    dbname="postgres", user="postgres", password="1111", host="localhost", port= "5433"
)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS snake(
            Name VARCHAR(50) NOT NULL,
            Score INT NOT NULL DEFAULT 0,
            Blocks INT NOT NULL 1);
            )""")

conn.commit()

cur.execute(""" INSERT INTO SNAKE (Name, Score, Blocks) VALUES (%s, %s, %s)""", ("Alica", 0, 1))

conn.commit()

cur.execute("""SELECT * FROM snake""")

row = cur.fetchall()

print(row[0])


# Получение пользователя
"""username = input("Enter your username: ")

cur.execute("SELECT id FROM users WHERE username = %s", (username,))
res = cur.fetchone()
if res:
    user_id = res[0]
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()

cur.execute("SELECT MAX(level) FROM scores WHERE user_id = %s", (user_id,))
level = cur.fetchone()[0] or 1

# Настройки уровня
speed = 10 + level * 2

# Инициализация pygame
pygame.init()
width, height = 600, 400
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake = [(100, 50)]
direction = (10, 0)
food = (300, 200)
score = 0

running = True
paused = False

font = pygame.font.SysFont('Arial', 25)

def draw():
    win.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(win, (0, 255, 0), (*segment, 10, 10))
    pygame.draw.rect(win, (255, 0, 0), (*food, 10, 10))
    text = font.render(f"Score: {score} Level: {level}", True, (255, 255, 255))
    win.blit(text, (10, 10))
    pygame.display.update()

while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: direction = (0, -10)
            if event.key == pygame.K_DOWN: direction = (0, 10)
            if event.key == pygame.K_LEFT: direction = (-10, 0)
            if event.key == pygame.K_RIGHT: direction = (10, 0)
            if event.key == pygame.K_p:
                # пауза и сохранение
                paused = True
                cur.execute("INSERT INTO scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                conn.commit()
                print("Game paused. Score saved.")
                pygame.quit()
                sys.exit()

    if not paused:
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        if head == food:
            score += 10
            food = (random.randint(0, 59)*10, random.randint(0, 39)*10)
        else:
            snake.pop()

        # Проверка на столкновение со стеной
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height or head in snake[1:]:
            print("Game Over")
            cur.execute("INSERT INTO scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
            conn.commit()
            pygame.quit()
            sys.exit()

        draw()

cur.close()
conn.close()"""