import time
import race_manager
import result
# v2

input_command = ""
race_manager = race_manager.RaceManager()
results = result.Result("race_results.txt")


def race():
    race_manager.reset_race()
    while not race_manager.race_over:
        race_manager.print_race()
        race_manager.move_cars()
        time.sleep(0.1)
    race_manager.print_race()
    print(f"Top 3 finishers:\n {results.get_results(race_manager.get_results())}\n")


while input_command != "3":

    while input_command not in ["1", "2", "3"]:
        input_command = input('Type "1" to have a race\n'
                              'Type "2" to see race history\n'
                              'Type "3" to exit program\n').lower()
    if input_command == "1":
        race()
        input_command = ""
    elif input_command == "2":
        results.print_race_results()
        input_command = ""
