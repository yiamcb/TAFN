def extract_nirs_features(nirs_data):
    features = []
    for sample in nirs_data:
        mean_features = np.mean(sample, axis=0).reshape(-1, 1)
        std_features = np.std(sample, axis=0).reshape(-1, 1)
        features.append(np.hstack((mean_features, std_features)))
    return np.array(features)
def NIRS_BandPowers(nirs_signal):
  fs = 10
  freq_range = [0, 0.2]  # Frequency range of interest in Hz
  sampling_freq = 10  # Sampling frequency in Hz

  Features = []
  for i_files in range(np.shape(nirs_signal)[0]):
    for i_frame in range(np.shape(nirs_signal[i_files])[0]):
      for i_channels in range(72):
        data_channel = np.array(nirs_signal[i_files])[i_frame,:,i_channels]
        sample_data = np.reshape(data_channel, [np.shape(data_channel)[0], 1])

        frequencies, psd = signal.welch(sample_data, fs=sampling_freq, axis=0)
        start_index = np.argmax(frequencies >= freq_range[0])
        end_index = np.argmax(frequencies >= freq_range[1])
        psd_normalized = psd / np.sum(psd[start_index:end_index], axis=0)

        spectral_entropy = -np.sum(psd_normalized * np.log2(psd_normalized), axis=0)

        peaks, _ = scipy.signal.find_peaks(sample_data.squeeze())
        avg_peaks_time = np.mean((peaks[1:]-peaks[0:-1])/fs)

        # Slope
        slope = np.diff(sample_data.squeeze())
        slope = np.mean(slope)

        # Area under the curve
        area = np.trapz(sample_data.squeeze())

        # Spectral Contrast
        f, t, Sxx = scipy.signal.spectrogram(sample_data.squeeze(), fs=fs, nperseg=256)
        spectral_contrast = np.mean(np.mean(np.diff(Sxx, axis=0), axis=1))

        # Spectral Flatness
        spectral_flatness = librosa.feature.spectral_flatness(y=sample_data.squeeze())[0]


        #Extracting Morlet Coefficients
        sps = 64
        morlet_coeffs = librosa.feature.melspectrogram(y=sample_data.squeeze(), sr=fs, n_mels=sps, fmin=1, fmax=fs/2, n_fft = 128)
        morlet_coeffs = np.reshape(morlet_coeffs, [sps])
        morlet_coeffs = np.mean(morlet_coeffs)

        # Mean
        mean_bin = np.mean(sample_data.squeeze(), axis=0)

        # Median
        median_bin = np.median(sample_data.squeeze(), axis=0)

        # Skewness
        features_skewness = np.mean((sample_data - np.mean(sample_data))**3) / np.power(np.var(sample_data), 1.5)

        # Zero-crossing rate
        zero_crossings = librosa.feature.zero_crossing_rate(sample_data)[0]
        features_zerocrossing = np.mean(zero_crossings)


        Outputs = np.array([spectral_entropy[0], avg_peaks_time, slope, area, spectral_contrast, spectral_flatness[0],
                            morlet_coeffs, mean_bin, median_bin, features_skewness, features_zerocrossing])


        Outputs = np.reshape(Outputs, [1, np.shape(Outputs)[0]])

        if i_channels == 0:
          Channels_Select = Outputs
        else:
          Channels_Select = np.concatenate((Channels_Select, Outputs), axis = 1)

      if i_frame == 0:
        Features_Frames = Channels_Select
      else:
        Features_Frames = np.concatenate((Features_Frames, Channels_Select), axis = 0)

    Features.append(Features_Frames)

  return Features