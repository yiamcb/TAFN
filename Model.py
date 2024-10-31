def tcn_layer(input_layer, num_filters=64, kernel_size=3, dilation_rate=1):
    conv = Conv1D(filters=num_filters, kernel_size=kernel_size, dilation_rate=dilation_rate, padding='causal', activation='relu')(input_layer)
    conv = BatchNormalization()(conv)  # Adding batch normalization
    return conv

def temporal_attention(input_layer):
    x = Permute((2, 1))(input_layer)
    x = Dense(1, activation='tanh')(x)
    x = Permute((2, 1))(x)
    x = Multiply()([input_layer, x])
    x = Activation('softmax')(x)
    return x

def CNN_EEG_NIRS_Testing(eeg_train, eeg_test, nirs_train, nirs_test, labels_train, labels_test):
    eeg_input_shape = np.shape(eeg_train)[1], np.shape(eeg_train)[2]
    nirs_input_shape = np.shape(nirs_train)[1], np.shape(nirs_train)[2]

    eeg_input = Input(shape=eeg_input_shape, name='eeg_input')
    eeg_tcn = tcn_layer(eeg_input)
    eeg_attention = temporal_attention(eeg_tcn)
    eeg_lstm = LSTM(64, return_sequences=True)(eeg_attention)
    eeg_flatten = Flatten()(eeg_lstm)

    nirs_input = Input(shape=nirs_input_shape, name='nirs_input')
    nirs_tcn = tcn_layer(nirs_input)
    nirs_attention = temporal_attention(nirs_tcn)
    nirs_lstm = LSTM(64, return_sequences=True)(nirs_attention)
    nirs_flatten = Flatten()(nirs_lstm)

    concatenated = Concatenate()([eeg_flatten, nirs_flatten])

    dense1 = Dense(32, activation='relu')(concatenated)
    # dense1 = BatchNormalization()(dense1)  # Adding batch normalization
    # dense1 = Dropout(0.5)(dense1)  # Adding dropout for regularization
    dense2 = Dense(32, activation='relu')(dense1)

    output = Dense(2, activation='sigmoid')(dense2)

    model = Model(inputs=[eeg_input, nirs_input], outputs=output)

    lr = 1e-4
    model.compile(loss=custom_loss(class_weights=[1, 1], asymmetric_weights=[1, 2], regularization_factor=0.0001), optimizer=optimizer, metrics=['accuracy'])

    return model