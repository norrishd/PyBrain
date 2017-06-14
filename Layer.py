import Neuron
import Parameters


class Layer:

    def __init__(self, layer, column):
        self.layer = layer
        self.column = column
        self.neurons = []

        # Check how many neurons the layer should have
        if self.layer == 1:
            number_of_neurons = Parameters.PYRAMIDALS_PER_COLUMN_LAYER_1
        elif self.layer == 2:
            number_of_neurons = Parameters.PYRAMIDALS_PER_COLUMN_LAYER_2
        else:
            number_of_neurons = Parameters.PYRAMIDALS_PER_COLUMN_LAYER_3

        for i in range(number_of_neurons):
            self.neurons.append(Neuron(self.layer, self.column))

    def get_neural_firing(self, inputs, time):
        """ Step the layer forward in time and check for neural firing
        
        :param inputs: 
        :param time: 
        :return: boolean list indicating firing pattern of all neurons in the current layer 
        """

        neural_firings = []
        for neuron in self.neurons:
            neural_firings.append(neuron.get_injected_potential(inputs, time))
        return neural_firings