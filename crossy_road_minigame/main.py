import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_manager.loop_count == 6:
        car_manager.new_car()
        car_manager.loop_count = 0
    else:
        car_manager.loop_count += 1

    car_manager.move_cars()

    if player.collision(car_manager.car_list):
        game_is_on = False
        scoreboard.game_over()

    elif player.cross_finish():
        player.reset()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()