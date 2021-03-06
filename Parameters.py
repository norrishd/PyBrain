""" Class to store physiological parameters accessed by all other classes.
    
    These can be tweaked to influence the effectiveness and resource demand of the entire system

"""

NUMBER_OF_COLUMNS = 10
PYRAMIDALS_PER_COLUMN_LAYER_1 = 10
PYRAMIDALS_PER_COLUMN_LAYER_2 = 10
PYRAMIDALS_PER_COLUMN_LAYER_3 = 1
NUMBER_OF_BRANCHES_PER_LAYER_1_PYRAMIDAL = 20
NUMBER_OF_BRANCHES_PER_LAYER_2_PYRAMIDAL = 10
NUMBER_OF_BRANCHES_PER_LAYER_3_PYRAMIDAL = 10
NUMBER_OF_CONDITION_DEFINING_INPUTS_PER_CORTICAL_LAYER_1_BRANCH = 25
NUMBER_OF_CONDITION_DEFINING_INPUTS_PER_CORTICAL_LAYER_2_BRANCH = 15
NUMBER_OF_CONDITION_DEFINING_INPUTS_PER_CORTICAL_LAYER_3_BRANCH = 15
CORTICAL_CONDITIONS_DEFINING_INPUT_WEIGHT = 1
INITIAL_LAYER_3_SYNAPTIC_WEIGHT = 1
MAXIMUM_BRANCH_SYNAPTIC_WEIGHT = 1.9
DENDRITIC_BRANCH_THRESHOLD_LAYER_1 = 450
DENDRITIC_BRANCH_THRESHOLD_LAYER_2 = 450
DENDRITIC_BRANCH_THRESHOLD_LAYER_3 = 400
CORTICAL_BASAL_DENDRITE_THRESHOLD = 985
CORTICAL_LAYER_3_BASAL_DENDRITE_THRESHOLD = 990
BRANCH_CONTRIBUTIONS_WITHIN_200MSEC_FOR_PERMANENT_WEIGHT_CHANGE = 3
BRANCH_FIRINGS_TO_DECREASE_IN_SYNAPTIC_WEIGHTS = 4
BDNF_INCREMENT_PER_FIRING = 0.5
BDNF_CONCENTRATION_REDUCTION_PER_TIME_SLOT = 0.9999
BDNF_CONCENTRATION_THRESHOLD_FOR_REDUCTION_IN_SYNAPTIC_WEIGHTS = 17.5
FREQUENT_FIRING_REDUCTION_IN_SYNAPTIC_WEIGHTS_PROPORTION = 0.9
BDNF_DECREMENT_FOLLOWING_WEIGHT_REDUCTION = 1
BIAS_ON_FAVOURED_INPUTS = 0
COLUMN_RECOMMENDATION_WEIGHT_GAIN_IN_GUIDED_LEARNING = 1.0
COLUMN_RECOMMENDATION_WEIGHT_REDUCTION_FACTOR_IN_NEGATIVE_FEEDBACK = 1.1

# Extra implcitly included in Andrew's model
NUMBER_OF_BASAL_GANGLIA = 10
NUMBER_OF_CATEGORIES = NUMBER_OF_BASAL_GANGLIA
NUMBER_OF_INPUT_CHANNELS = 200
AVG_SPIKES_PER_SEC_PER_INPUT_CHANNEL = 25
MSEC_IN_SIMULATION = 200
SIMULATION_UPDATES_PER_MSEC = 3