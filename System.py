import Parameters
import Column
import Category


class System:
    """ Class for the overall system; contain information on all categories, synapses, branches, neurons, layers and
        columns.
        
        (System) -> None
    """

    def __init__(self):
        self.categories = []
        self.input_channel_states = []
        self.columns = []

        # Randomly generate all categories and columns
        for i in range(Parameters.NUMBER_OF_CATEGORIES):
            self.categories.append(Category.Category())

        for i in range(Parameters.NUMBER_OF_COLUMNS):
            self.columns.append(Column.Column(i))

    # default value seemed necessary to stop PyCharm complaining that the method couldn't be accessed
    def step(self, time, current_category=0):
        """ Steps the system forward in time
        
        :return: None
        """

        # Update channel categories
        input_channels = self.categories[current_category].get_channel_firings()
        column_outputs = []
        for column in self.columns:
            column_outputs.append(column.get_injected_potential(input_channels, time))
        return column_outputs
