import Layer
import Parameters


class Column:

    def __init__(self, column_number):
        self.column_number = column_number
        self.layer1 = Layer(1, self.column_number)
        self.layer2 = Layer(2, self.column_number)
        self.layer3 = Layer(3, self.column_number)
        self.basal_ganglia_recommendation_weights = []

        # Where 10 is the number of basal
        for i in range(10):
            # TODO determine how these weights are initialised
            self.basal_ganglia_recommendation_weights = 1.0

    def step(self, input_channels, time):
        """ Steps the system forward in time, passing down the firing status of the previous layer (either input
            channels or prevous neuron layer) and current time of the system
        
        :param input_channels: a boolean list of which which input channels have just fired 
        :param time: current timeslot of the system
        :return: a (1-element) boolean list of whether layer 3 fired in this time step
        """

        layer1_firings = self.layer1.get_injected_potential(input_channels, time)
        layer2_firings = self.layer2.get_injected_potential(layer1_firings, time)
        layer3_firings = self.layer3.get_injected_potential(layer2_firings, time)

        return layer3_firings
