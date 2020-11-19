import pyglet
import random
import math
game_window = pyglet.window.Window(800,600)
    

# Muda o index da pasta de recursos de modo relativo a este arquivo
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("Player.png")
bullet_image = pyglet.resource.image("Bullet.png")
asteroid_image = pyglet.resource.image("Asteroid.png")

# O ponto da imagem considerado agora é sempre o meio
def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)


# retorna a distância entre dois pontos
def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

# Cria o lote principal
main_batch = pyglet.graphics.Batch()

# Coloca a legenda de pontos e título
score_label = pyglet.text.Label(text="Score: 0", x=10, y=460, batch = main_batch)
level_label = pyglet.text.Label(text="Asteroids V1.0.0", x=game_window.width//2, y=game_window.height//2, anchor_x='center', batch = main_batch)

# Cria o sprite do jogador no meio da tela
player_ship = pyglet.sprite.Sprite(img=player_image, x=400, y=300,batch = main_batch)

# Cria um número de asteroides em lugares aleatórios da tela. Não coloca exatamente em cima do jogador
def Asteroids(num_asteroids,player_position, batch = None):
    asteroids = []
    for _ in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=asteroid_image,
                                            x=asteroid_x, y=asteroid_y, batch = batch)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids

# Cria o sprite dos asteroids
asteroids = Asteroids(3, player_ship.position, main_batch)

# Coloca os sprites da vida do jogador em uma lista
def Player_lives(num_icons, batch=None):
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=player_image,
                                          x=785-i*30, y=585, batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives

# Cria o sprite das vidas
player_lives = Player_lives(3,main_batch)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()










if __name__ == '__main__':
    pyglet.app.run()