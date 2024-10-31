def ApplyBandPass(Data_EEG):

  fs = 200

  # Define the bandpass filter specifications
  lowcut = 1    # Lower cutoff frequency (in Hz)
  highcut = 45  # Upper cutoff frequency (in Hz)
  order = 4     # Filter order (you can adjust this value as needed)

  nyquist = 0.5 * fs

  # Normalize the cutoff frequencies to the Nyquist frequency
  lowcut_normalized = lowcut / nyquist
  highcut_normalized = highcut / nyquist


  # Design the bandpass Butterworth filter
  b, a = signal.butter(order, [lowcut_normalized, highcut_normalized], btype='band')

  # Apply the bandpass filter to array and each channel
  Filtered_Data = [apply_bandpass_filter(data_array, b, a) for data_array in Data_EEG]

  return Filtered_Data