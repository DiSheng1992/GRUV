from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM, GRU


def create_lstm_network(num_frequency_dimensions, num_hidden_dimensions, data_size, num_recurrent_units=1):
    model = Sequential()
    # This layer converts frequency space to hidden space
    model.add(Dense(num_hidden_dimensions, input_shape=(data_size, num_frequency_dimensions)))
    #model.add(TimeDistributedDense(input_dim=num_frequency_dimensions, output_dim=num_hidden_dimensions))
    for cur_unit in range(num_recurrent_units):
        model.add(LSTM(input_dim=num_hidden_dimensions, output_dim=num_hidden_dimensions, return_sequences=True))
    # This layer converts hidden space back to frequency space
    model.add(Dense(num_frequency_dimensions))
    #model.add(TimeDistributedDense(input_dim=num_hidden_dimensions, output_dim=num_frequency_dimensions))
    model.compile(loss='mean_squared_error', optimizer='rmsprop')
    return model


def create_gru_network(num_frequency_dimensions, num_hidden_dimensions, data_size, num_recurrent_units=1):
    model = Sequential()
    # This layer converts frequency space to hidden space
    model.add(Dense(num_hidden_dimensions, input_shape=(data_size, num_frequency_dimensions)))
    #model.add(TimeDistributedDense(input_dim=num_frequency_dimensions, output_dim=num_hidden_dimensions))
    for cur_unit in range(num_recurrent_units):
        model.add(GRU(input_dim=num_hidden_dimensions, output_dim=num_hidden_dimensions, return_sequences=True))
    # This layer converts hidden space back to frequency space
    model.add(Dense(num_frequency_dimensions))
    #model.add(TimeDistributedDense(input_dim=num_hidden_dimensions, output_dim=num_frequency_dimensions))
    model.compile(loss='mean_squared_error', optimizer='rmsprop')
    return model
