import pygame
import random
import math
from copy import deepcopy
from data.merge_move import MergeMove
from data.settings import *

pygame.init()


class Main:
    def __init__(self):
        self.board = Board()
        self.screen = Screen()

    def game_loop(self):
        self.screen.render()
        self.board.draw()


class Board(MergeMove):
    def __init__(self):
        super(Board, self).__init__()

        self.next_nums = []

        self.images = [
            pygame.image.load('data/img/numbers/2.png'),
            pygame.image.load('data/img/numbers/4.png'),
            pygame.image.load('data/img/numbers/8.png'),
            pygame.image.load('data/img/numbers/16.png'),
            pygame.image.load('data/img/numbers/32.png'),
            pygame.image.load('data/img/numbers/64.png'),
            pygame.image.load('data/img/numbers/128.png'),
            pygame.image.load('data/img/numbers/256.png'),
            pygame.image.load('data/img/numbers/512.png'),
            pygame.image.load('data/img/numbers/1024.png'),
            pygame.image.load('data/img/numbers/2048.png'), ]

        self.initialize()
        self.draw()

    def initialize(self):
        initial_numbers = random.choices([2, 4], weights=[3, 1], k=2)
        initial_positions = [[random.choice(range(4)), random.choice(range(4))], [random.choice(range(4)),
                                                                                  random.choice(range(4))]]

        while initial_positions[0] == initial_positions[1]:
            initial_positions[1] = [random.choice(range(4)), random.choice(range(4))]

        self.board[initial_positions[0][0]][initial_positions[0][1]] = initial_numbers[0]
        self.board[initial_positions[1][0]][initial_positions[1][1]] = initial_numbers[1]

    def draw(self):
        for row_idx, row in enumerate(self.board):
            for index, num in enumerate(row):
                if num != 0:
                    img_idx = self._get_index(num)
                    screen.blit(self.images[img_idx],
                                (
                                    WIDTH / 4 + (100 * index) + (10 * index) - 10,
                                    HEIGHT / 4 + (100 * row_idx) + (10 * row_idx) - 61
                                ))

    def _get_index(self, num):
        return int(math.log(num, 2)) - 1

    def move(self, direction):
        self.move_tiles(direction)

        if self.board != self.previous_board:  # don't spawn nums in useless moves
            self.spawn_num()

    def board_full(self):
        return 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2] and 0 not in self.board[3]

    def spawn_num(self):
        index = random.randint(0, 3)
        while 0 not in self.board[index]:
            index = random.randint(0, 3)

        row = self.board[index]

        indices = [i for i, x in enumerate(row) if x == 0]

        col = random.choice(indices)

        if len(self.next_nums) == 0:
            self._generate_nums()

        self.board[index][col] = self.next_nums[0]
        self.next_nums.pop(0)

    def _generate_nums(self):
        # The numbers are generated in batch so that if the user undoes, the next number is always the same
        self.next_nums = random.choices((2, 4), weights=(3, 1), k=4)


class Screen:
    def __init__(self):
        self.bg = pygame.image.load('data/img/bg.png').convert()
        self.big_font = pygame.font.Font('data/Typo_Round.otf', 50)
        self.small_font = pygame.font.Font('data/Typo_Round.otf', 30)
        self.title = self.big_font.render('2048', True, (50, 50, 50))
        self.move = self.small_font.render('Arrow keys or wasd to move', True, (50, 50, 50))
        self.undo = self.small_font.render('Z to undo', True, (50, 50, 50))
        self.restart = self.small_font.render('R to restart', True, (50, 50, 50))

    def render(self):
        screen.blit(self.bg, (180, 80))
        screen.blit(self.title, (345, 20))
        screen.blit(self.undo, (10, 550))
        screen.blit(self.move, (210, 550))
        screen.blit(self.restart, (650, 550))


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                main.board.move('UP')
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main.board.move('RIGHT')
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                main.board.move('DOWN')
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main.board.move('LEFT')

            if event.key == pygame.K_r:
                main.board.board = deepcopy(BOARD_INIT)
                main.board.initialize()

            if event.key == pygame.K_z:
                if main.board.previous_board:  # You cant undo if you haven't moved ;)
                    main.board.board = main.board.previous_board


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
main = Main()

while True:
    events()
    clock.tick(FPS)
    screen.fill((200, 200, 200))
    main.game_loop()
    pygame.display.update()
