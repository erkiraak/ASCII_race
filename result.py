import time
import pandas


class Result:
    def __init__(self, filename):
        self.file_name = filename
        self.check_file()
        self.race_number = None
        self.race_results = pandas.DataFrame

    def check_file(self):
        """
        Checks if results file exist. If not, creates it based on filename specified while creating item
        """
        import os
        if os.path.isfile(self.file_name) and os.stat(self.file_name).st_size != 0:
            pass
        else:
            with open(self.file_name, "w") as race_results_empty:
                race_results_empty.write("Race results:\n")

    def print_race_results(self):
        """
        Opens results file and prints it. If the file contains only title row, prints appropriate message
        """
        with open(self.file_name, "r") as race_results:
            result_list = race_results.readlines()
            if len(result_list) == 1:
                print("\nNo races held yet!\n")
                return
            for row in result_list:
                print(row, end="")

    def write_race_results(self, result_string):
        """
        Appends passed result string to result text file with a race timestamp
        """
        with open(self.file_name, "a") as race_results:
            race_results.write(
                f"\n"
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} race results:\n"
                f"{result_string}\n")

    def get_results(self, dict_original):
        """
        Creates a pandas dataframe from passed race results dictionary.
        Sorts dataframe based on race time and cars position after finish
        Resets index and adds 1 to new index to create finish positions and trims extra columns
        Saves a full finishers list in string format to parameter
        Returns dataframe of top 3 finishers
        """
        results_dataframe = pandas.DataFrame.from_dict(dict_original, orient="index")
        results_dataframe = results_dataframe.sort_values(by=["Time", "Finish_position"])
        results_dataframe = results_dataframe.reset_index(drop=True)
        results_dataframe.index = results_dataframe.index + 1
        results_dataframe = results_dataframe.drop(columns=["Finish_position"])
        results_dataframe = results_dataframe.round(2)
        results_top_3 = results_dataframe.iloc[:3]
        self.write_race_results(results_dataframe.to_string())
        return results_top_3
