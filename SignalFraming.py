""" Creating data frames with overlapping windows"""


def FramedData(Filtered_Data, fs):

  """ Framing the Data"""

  frame_duration = 2.5  # Frame duration in seconds
  overlap_duration = 1  # Overlap duration in seconds

  frame_length = int(fs * frame_duration)
  hop_length = int(fs * (frame_duration - overlap_duration))

  Framed_Data = []
  for array in Filtered_Data:
      framed_array = frame_signal(array, frame_length, hop_length)
      Framed_Data.append(framed_array)

  #All arrays inside list need to be of the same size, so executing the code below.
  min_size = min(arr.shape[0] for arr in Framed_Data)
  Framed_Data = [arr[:min_size] for arr in Framed_Data]

  return Framed_Data

