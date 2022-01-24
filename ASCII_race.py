import time
import race_manager
import result

NUMBER_OF_RACERS = 10  # MAX 10
TRACK_MIN_LENGTH = 30
TRACK_MAX_LENGTH = 100
CAR_MIN_SPEED = 3
CAR_MAX_SPEED = 10
DRIVER_DATA = {
    1: {
        "name": "Tänak",
        "symbol": "T"
    },
    2: {
        "name": "Ogier",
        "symbol": "O"
    },
    3: {
        "name": "Loeb",
        "symbol": "L"
    },
    4: {
        "name": "Neuville",
        "symbol": "N"
    },
    5: {
        "name": "Rovanpara",
        "symbol": "R"
    },
    6: {
        "name": "Evans",
        "symbol": "E"
    },
    7: {
        "name": "Breen",
        "symbol": "B"
    },
    8: {
        "name": "Greensmith",
        "symbol": "G"
    },
    9: {
        "name": "Meeke",
        "symbol": "M"
    },
    10: {
        "name": "Sordo",
        "symbol": "S"
    }
}

input_command = ""
race_manager = race_manager.RaceManager(
    track_min_length=TRACK_MIN_LENGTH,
    track_max_length=TRACK_MAX_LENGTH
)
for i in range(1, NUMBER_OF_RACERS + 1):
    race_manager.add_car(
        number=i,
        image=DRIVER_DATA.get(i).get("symbol"),
        driver_name=DRIVER_DATA.get(i).get("name"),
        min_speed=CAR_MIN_SPEED,
        max_speed=CAR_MAX_SPEED,
    )
    race_manager.add_track(
        number=i,
        car_image=DRIVER_DATA.get(i).get("symbol")
    )
results = result.Result("race_results.txt")


def race():
    race_manager.reset_race()
    while not race_manager.race_over:
        race_manager.print_race()
        race_manager.move_cars()
        time.sleep(0.25)
    race_manager.print_race()
    print(f"Top 3 finishers:\n {results.get_results(race_manager.get_results())}\n")


while input_command != "exit":

    while input_command not in ["race", "history", "exit"]:
        input_command = input('Type "Race" to have a race\n'
                              'Type "History" to see race history\n'
                              'Type "Exit" to exit program\n').lower()
    if input_command == "race":
        race()
        input_command = ""
    elif input_command == "history":
        results.print_race_results()
        input_command = ""
