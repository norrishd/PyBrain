import Synapse
import Parameters


class Branch:

    def __init__(self, layer, column):
        """ Instantiate a new Branch of a Neuron's basal dendrite.
        
            All Branches inject the same amount of potential into the dendritic tree if they exceed their
            firing threshold.
        
            (Branch) -> None
        """
        self.layer = layer
        self.column = column
        self.synapses = []
        self.total_branch_potential = 0.0
        self.currently_injecting_potential = False
        self.time_start_current_injection = None

        if self.layer == 1:
            number_of_synapses = Parameters.NUMBER_OF_CONDITION_DEFINING_INPUTS_PER_CORTICAL_LAYER_1_BRANCH
            self.threshold = Parameters.DENDRITIC_BRANCH_THRESHOLD_LAYER_1
        elif self.layer == 2:
            number_of_synapses = Parameters.NUMBER_OF_CONDITION_DEFINING_INPUTS_PER_CORTICAL_LAYER_2_BRANCH
            self.threshold = Parameters.DENDRITIC_BRANCH_THRESHOLD_LAYER_2
        else:
            number_of_synapses = Parameters.NUMBER_OF_CONDITION_DEFINING_INPUTS_PER_CORTICAL_LAYER_3_BRANCH
            self.threshold = Parameters.DENDRITIC_BRANCH_THRESHOLD_LAYER_3

        for i in range(number_of_synapses):
            self.synapses.append(Synapse.Synapse(self.layer, self.column))

    def get_branch_potential(self, higher_layer_input, time):
        """ Get potential injected from branch to dendritic tree at the current time as a result of input from higher
            layer neurons or channels
        
        :param higher_layer_input: 
        :param time: current time slot of the system
        :return: a double indicating total potential being injected into the dendritic tree
        """

        # Get total current branch potential
        new_branch_potential = 0.0
        for synapse in self.synapses:
            new_branch_potential += synapse.get_injected_potential(higher_layer_input, time)
        self.total_branch_potential = new_branch_potential

        # Get potential for this branch
        if self.total_branch_potential > self.threshold:
            # TODO implement probabilistic injection, with prob increasing to 1 by 1.1x threshold value
            self.currently_injecting_potential = True
            self.time_start_current_injection = time

        if self.currently_injecting_potential:
            # TODO this should return some value multiplied by some fractional multiplier as a function of time
            if time > self.time_start_current_injection + 4:
                self.currently_injecting_potential = False
            return 400
        else:
            return 0.0

    def modify_synaptic_weights(self, action_potential_init_time):
        for synapse in self.synapses:
            synapse.modify_synaptic_weight(action_potential_init_time)
