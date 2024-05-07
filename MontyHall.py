import numpy as np
import pandas as pd
import logging

# Configure logging to provide timestamp, logging level, and message.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MontyHallSimulator:
    """
    A simulator for the Monty Hall problem that demonstrates the effect of switching versus staying on the probability of winning.

    Attributes:
        num_trials (int): Number of trials to simulate.
        verbose (bool): Flag to turn on/off the logging of messages for simulation operations.
        dataframe (DataFrame): Stores the results of all simulations.
    """

    def __init__(self, num_trials, verbose=True):
        """
        Initializes the Monty Hall Simulator with the specified number of trials and verbosity.

        Args:
            num_trials (int): The number of trials to run the simulation.
            verbose (bool): If True, enables logging of informational messages.
        """
        self.num_trials = num_trials
        self.verbose = verbose
        self.dataframe = pd.DataFrame()
        if self.verbose:
            logging.info(f"Simulator initialized for {num_trials} trials.")

    def simulate_trial(self):
        """
        Simulates a single trial of the Monty Hall problem.

        Returns:
            dict: A dictionary containing the results of the trial, including doors configuration,
            player's choice, host's opened door, the remaining door, and outcomes of staying or switching.
        """
        doors = [0, 0, 1]  # Assume 1 is the car, 0s are goats
        np.random.shuffle(doors)
        player_choice = np.random.randint(0, 3)
        car_position = doors.index(1)
        possible_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
        host_opens = np.random.choice(possible_doors)
        remaining_door = 3 - player_choice - host_opens
        stay_win = int(player_choice == car_position)
        switch_win = int(remaining_door == car_position)

        return {
            'Doors Configuration': ''.join(str(d) for d in doors),
            'Player Choice': player_choice + 1,
            'Host Opens': host_opens + 1,
            'Remaining Door': remaining_door + 1,
            'Stay Win': stay_win,
            'Switch Win': switch_win
        }

    def run_simulation(self):
        """
        Runs the simulation for the configured number of trials and stores results in a DataFrame.
        """
        results = [self.simulate_trial() for _ in range(self.num_trials)]
        self.dataframe = pd.DataFrame(results)
        if self.verbose:
            logging.info("Simulation completed.")

    def calculate_statistics(self):
        """
        Calculates and logs the winning percentages for staying and switching strategies.

        Returns:
            tuple: A tuple containing the stay and switch win percentages.
        """
        stay_wins = self.dataframe['Stay Win'].sum()
        switch_wins = self.dataframe['Switch Win'].sum()
        stay_win_percentage = (stay_wins / self.num_trials) * 100
        switch_win_percentage = (switch_wins / self.num_trials) * 100
        if self.verbose:
            logging.info(f"Statistics calculated: Stay {stay_win_percentage}%, Switch {switch_win_percentage}%")
        return stay_win_percentage, switch_win_percentage

    def print_results(self):
        """
        Prints the results of the simulation and handles any exceptions during result calculation.
        """
        try:
            stay_percentage, switch_percentage = self.calculate_statistics()
            print(f"Results after {self.num_trials} trials:")
            print(f"Winning by Staying: {stay_percentage:.2f}%")
            print(f"Winning by Switching: {switch_percentage:.2f}%")
        except Exception as e:
            if self.verbose:
                logging.error("Error in printing results: ", exc_info=True)

# Example usage and simulation for multiple sets of trials:
if __name__ == "__main__":
    trials = [1000, 10000, 100000, 1000000]
    for num_trials in trials:
        simulator = MontyHallSimulator(num_trials, verbose=False)
        simulator.run_simulation()
        simulator.print_results()
        print('\n')
