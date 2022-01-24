import random


class Car:
    def __init__(self, image, name, car_number, min_speed, max_speed):
        self.image = image
        self.driver = name
        self.car_number = car_number
        self.position = 0
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.finished = False
        self.start_time = None
        self.finish_time = None
        self.race_time = None
        self.position_after_finish = None

    def move_car(self):
        """Moves car by random amount between min and max speed"""
        self.position += random.randint(self.min_speed, self.max_speed)

    def set_car_position(self, position):
        self.position = position

    def set_car_finished_status(self, state):
        self.finished = state
