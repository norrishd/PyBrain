import Branch
import Parameters


class Neuron:

    def __init__(self, layer, column):
        """ Instantiate a new Neuron
        
            (Neuron) -> None
        """
        self.layer = layer
        self.column = column
        self.branches = []
        self.currently_firing = False
        self.total_dendritic_potential = 0.0
        # brain-derived neurotrophic factor, which will decrease branch synaptic weights if exceeds threshold
        self.BDRF = 0.0

        # Refer to physiological parameters to determine how many dendritic branches neuron should have
        if self.layer == 1:
            number_of_branches = Parameters.NUMBER_OF_BRANCHES_PER_LAYER_1_PYRAMIDAL
            self.threshold = Parameters.CORTICAL_BASAL_DENDRITE_THRESHOLD
        elif self.layer == 2:
            number_of_branches = Parameters.NUMBER_OF_BRANCHES_PER_LAYER_2_PYRAMIDAL
            self.threshold = Parameters.CORTICAL_BASAL_DENDRITE_THRESHOLD
        else:
            number_of_branches = Parameters.NUMBER_OF_BRANCHES_PER_LAYER_3_PYRAMIDAL
            self.threshold = Parameters.CORTICAL_LAYER_3_BASAL_DENDRITE_THRESHOLD

        for i in range(number_of_branches):
            self.branches.append(Branch.Branch(self.layer, self.column))

    def get_dendritic_potential(self, input_channels, time):
        """ Step the system forward in time one third of a millisecond.
            If dendritic potential exceeds neuronal threshold, trigger an action potential
        
        :param input_channels: 
        :param time: current time slot of the simulation
        :return: boolean indicating if new action potential
        """
        new_dendritic_potential = 0.0
        for branch in self.branches:
            new_dendritic_potential += branch.get_injected_potential(input_channels, time)
        self.total_dendritic_potential = new_dendritic_potential

        if self.total_dendritic_potential > self.threshold:
            self.modify_input_synapse_weights(time)
            return True
        else:
            return False

    def modify_input_synapse_weights(self, time):
        for branch in self.branches:
            branch.modify_synaptic_weights(time)
