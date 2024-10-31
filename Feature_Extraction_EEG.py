def extract_features(eeg_signal, sampling_rate):
    Features = []
    for i_files in range(np.shape(eeg_signal)[0]):
      for i_frame in range(np.shape(eeg_signal[i_files])[0]):
        for i_channels in range(30):
          data_channel = np.array(eeg_signal[i_files])[i_frame,:,i_channels]

          sample_data = np.reshape(data_channel, [np.shape(data_channel)[0], 1])

          Power_alpha = bandpower(sample_data, fs, 8, 14)                 #Alpha Band Power
          Power_beta = bandpower(sample_data, fs, 14, 30)                 #Beta Band Power
          Power_alpha_beta = Power_alpha/Power_beta                       #Ratios


          sample_data = data_channel
          # Peaks
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


          Outputs = np.array([Power_alpha, Power_alpha_beta, avg_peaks_time, slope, area, spectral_contrast, spectral_flatness,
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