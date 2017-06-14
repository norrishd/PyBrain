import Parameters
import System

system = System()
runtime = Parameters.MSEC_IN_SIMULATION * Parameters.SIMULATION_UPDATES_PER_MSEC


def type_a_simulation():
    number_of_repetitions = 10

    # Loop through number of reps
    for i in range(number_of_repetitions):
        # Loop through each category sequentially
        for category in range(Parameters.NUMBER_OF_CATEGORIES):
            # Run 200 msec of simulation for a given category
            for time in range(runtime):
                cortical_outputs = system.step(time, category)

                # TODO check if outputs correctly pick category; adjust learning weights accordingly

            # Reverse weight gains for synapses which didn't contribute enough times


# TODO implement all this
def type_b_simulation():
    for time in range(runtime):
        print("Running type B simulation")