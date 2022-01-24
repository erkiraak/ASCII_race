import os
import time
import random
import racecar
import racetrack


class RaceManager:
    def __init__(self, track_min_length, track_max_length):
        self.cars = []
        self.tracks = []
        self.track_min_length = track_min_length
        self.track_max_length = track_max_length
        self.track_length = None
        self.set_track_length()
        self.race_over = False

    def add_car(self, number, image, driver_name, min_speed, max_speed):
        """
        Creates a Car item and adds it to track list
        Accepts car number, driver symbol, driver name, car minimal speed and car maximal speed
        """
        car = racecar.Car(
            car_number=number,
            image=image,
            name=driver_name,
            min_speed=min_speed,
            max_speed=max_speed
        )
        self.cars.append(car)

    def add_track(self, number, car_image):
        """
        Creates a Racetrack item and adds it to track list
        Accepts track number and car image as input
        """
        track = racetrack.Racetrack(
            track_number=number,
            image=car_image,
            length=self.track_length
        )
        self.tracks.append(track)

    def move_cars(self):
        """
        Moves every car in list, adds starting times if car position is 0.
        If car is finished, adds "Finished" flag and records race time.
        To keep car on screen and avoid index errors, resets the position to last position of track.
        In case all cars in list are "Finished", adds "Race over" flag.
        """
        self.race_over = True
        for car in self.cars:
            if car.position == 0:
                car.start_time = time.time()
            car.move_car()
            if car.position >= self.track_length:
                if not car.finished:
                    car.finish_time = time.time()
                    car.race_time = car.finish_time - car.start_time
                    car.set_car_finished_status(True)
                    car.position_after_finish = car.position
                car.set_car_position(self.track_length)
            if not car.finished:
                self.race_over = False

    def print_race(self):
        """Updates and prints racetrack strings"""
        os.system("cls")
        for track in self.tracks:
            track.update_track(self.cars[track.track_number - 1].position)
            print(track.track_string)

    def set_car_position(self, position):
        """Moves all cars to certain position"""
        for car in self.cars:
            car.set_car_position(position)

    def set_track_length(self):
        """Sets new track length"""

        self.track_length = random.randint(self.track_min_length, self.track_max_length)

    def reset_race(self):
        """Sets new track length and resets cars and tracks to beginning of race"""
        self.set_track_length()
        self.race_over = False
        for car in self.cars:
            car.set_car_position(0)
            car.set_car_finished_status(False)
        for track in self.tracks:
            track.change_track_length(self.track_length)

    def get_results(self):
        """
        Returns a dictionary containing last races times, driver name and symbol on track
        To allow determining position in case of equal race times, car position after finish is added
        """
        results = {}
        for car in self.cars:
            results[car.car_number - 1] = {
                "Driver": car.driver,
                "Symbol": car.image,
                "Time": car.race_time,
                "Finish_position": -car.position_after_finish
            }
        return results
