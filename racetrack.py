class Racetrack:
    def __init__(self, length, image, track_number):
        self.change_track_length(length)
        self.car_image: str = image
        self.update_track(0)
        self.track_number = track_number
        self.track_string = None
        self.track = None
        self.base_track = None
        self.track_length = None

    def update_track(self, position):
        """
        Makes a copy of base track, adds the car to track and joins the track list to string for easier printing
        """
        self.track = self.base_track.copy()
        self.track[position] = self.car_image
        self.track_string = "".join(self.track)

    def change_track_length(self, length):
        """Generates a new base track based on track length"""
        self.track_length = length
        self.base_track = ["_" if i < self.track_length else "|" for i in range(self.track_length + 1)]
