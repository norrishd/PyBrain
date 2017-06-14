import random
import Parameters


class Category:
    """ A class to represent a "category" of objects (e.g. cat, tree, guitar)
    
        Represented by a list of probabilities of firing across 200 channels at any given moment
        Firing probabilities are generated within a range such that the average firing rate across all channels
        will be approximately 25 firings per second
    """

    def __init__(self):
        """ Generate a new category
            
            (Category) -> None
        """
        self.channels_probs = []
        self.current_channel_firings = []

        # See working below
        expected_total_spikes = Parameters.AVG_SPIKES_PER_SEC_PER_INPUT_CHANNEL * (Parameters.MSEC_IN_SIMULATION / 1000)
        timeslots = Parameters.MSEC_IN_SIMULATION * Parameters.SIMULATION_UPDATES_PER_MSEC
        expected_spikes_per_timeslot = expected_total_spikes / timeslots

        for i in range(Parameters.NUMBER_OF_INPUT_CHANNELS):
            self.channels_probs.append(random.uniform(0, 2 * expected_spikes_per_timeslot))

        for i in range(Parameters.NUMBER_OF_INPUT_CHANNELS):
            self.current_channel_firings[i] = False

    def get_channel_firings(self):
        for i in range(self.channels_probs):
            if random.random() < self.channels_probs[i]:
                self.current_channel_firings[i] = True
            else:
                self.current_channel_firings[i] = False

        return self.current_channel_firings

'''
The simulation is tweaked so that there is an average of 25 spikes per second  across all channels
=> Therefore expect 5 spikes per channel across the 200 msec simulation
=> System has its state updated 3 times per msec, giving a total of 600 time slot
=> Therefore the average probability of a spike at any channel at a given time slot is 5/600 ~= 0.008333333333333333

Andrew Coward's model enforces a range of 0.0001 - 0.02. Here we use a simplified range of 0 to 2*(5/600) ~= 0.01666666

'''
