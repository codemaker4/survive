print('init')
import pygame
pygame.init()

screenWidth = 800
screenHight = 600
gameDisplay = pygame.display.set_mode((screenWidth,screenHight))
pygame.display.set_caption('LOADING...')

world = []
blocks = [['stone', [100, 100, 100], [['smallStonePickaxe', 8], ['stonePickaxe', 2]]], ['dirt', [100, 50, 0], [['bareHands', 10], ['woodShovel', 5], ['stoneShovel', 3]]], ['leaves', [50, 255, 50], [['bareHands', 5], []]]]
