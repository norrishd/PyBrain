import Parameters
import random


class Synapse:

    def __init__(self, layer, column):
        """ Instantiate a new synapse.
        
            (Synapse, int, double) -> None
        """
        self.layer = layer
        self.column = column

        if layer == 1:
            self.weight = Parameters.CORTICAL_CONDITIONS_DEFINING_INPUT_WEIGHT
            self.threshold = Parameters.DENDRITIC_BRANCH_THRESHOLD_LAYER_1
        elif layer == 2:
            self.weight = Parameters.CORTICAL_CONDITIONS_DEFINING_INPUT_WEIGHT
            self.threshold = Parameters.DENDRITIC_BRANCH_THRESHOLD_LAYER_2
        else:
            self.weight = Parameters.INITIAL_LAYER_3_SYNAPTIC_WEIGHT
        self.threshold = Parameters.DENDRITIC_BRANCH_THRESHOLD_LAYER_3
        # Used to revert weight gains if synapse doesn't contribute enough times this run
        self.initial_weight_this_simulation = self.weight
        self.contributions_to_action_potentials_this_run = 0
        # Used to reduce weight if multiple neuron firings but synapse did not contribute
        self.neuron_firings_without_contributing = 0
        self.presynaptic_input_index = self.pick_input()
        self.currently_injecting_potential = False
        self.time_start_latest_injection = None
        self.time_last_contributed_to_action_potential = None

    def pick_input(self):
        """ Picks a random input from the preceding layer of neurons.
            If layer 1, inputs will be selected from the 200 input channels
        
        :return: an int indicating the index of the input from the preceding layer
        """
        if self.layer == 1:
            # Where 200 input channels are assumed
            # TODO allow bias to improve input selection
            return random.randint(0, 199)
        elif self.layer == 2:
            # TODO confirm that inputs are simply the outputs from higher layer neurons
            return random.randint(0, Parameters.PYRAMIDALS_PER_COLUMN_LAYER_1)
        else:
            return random.randint(0, Parameters.PYRAMIDALS_PER_COLUMN_LAYER_2)

    def get_injected_potential(self, higher_layer_input, time):
        """ Step the system forward in time one third of a millisecond
            Takes current input and simulation time, and 
        
        :param higher_layer_input: boolean list of presynaptic potentials from higher layer,
        whether the input channels (for layer 1 neurons) or higher layer neurons (for layer 2/3 neurons)
        :param time: current time slot of the simulation
        :return: A float indicating the amount of injected potential from this synapse in the current time slot 
        """
        # Check if just received an input and update what's being injected into the branch
        # TODO implement mathematical injection of potential over time, which will require this variable. Currently just injecting instantly in the current time slot
        if higher_layer_input[self.presynaptic_input_index]:
            self.currently_injecting_potential = True
            self.time_start_latest_injection = time

        if self.currently_injecting_potential:
            # TODO this should return weight multiplied by some fractional multiplier as a function of time
            if time > self.time_start_latest_injection + 4:
                self.currently_injecting_potential = False
            return self.weight
        else:
            return 0.0

    def modify_synaptic_weight(self, action_potential_init_time):
        """ The neuron has just fired an action potential.
        
        "Backpropagation" checks if each synapse contributed to the action potential. 
        If contributed and is below the maximum weight threshold, increase weight
        If hasn't contributed recently enough, reduce weight
        
        :return: None
        """
        # If contributed within the last 5 milliseconds (5 msec * 3 updates per msec)
        if action_potential_init_time < self.time_start_latest_injection + 15:
            self.contributions_to_action_potentials_this_run += 1
            if self.weight < self.threshold:
                # TODO Implement mathematical function to change weight as a function of proximity to action potential triggering
                self.weight = self.weight * 1.1
            # Reduce weight back to threshold if overshot it earlier
            elif self.weight > self.threshold:
                self.weight = self.threshold

        # Didn't contribute within last 5 milliseconds
        else:
            self.neuron_firings_without_contributing += 1
            if self.neuron_firings_without_contributing >= Parameters.BRANCH_FIRINGS_TO_DECREASE_IN_SYNAPTIC_WEIGHTS:
                self.weight = self.weight * 0.9
