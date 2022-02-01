import time
import race_manager
import result


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
