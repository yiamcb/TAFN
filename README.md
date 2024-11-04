# TAFN
Temporal Attention Fusion Network with custom loss function for EEG-fNIRS classification

This study propose a novel temporal attention fusion network (TAFN) with a custom loss function. The TAFN model incorporates attention mechanisms to its long short-term memory and temporal convolutional layers to accurately capture spatial and temporal dependencies in the EEG–fNIRS data. The custom loss function combines class weights and asymmetric loss terms to ensure the precise classification of cognitive and motor intentions, along with addressing class imbalance issues.

# TAFN dataset processing utilities
This repository contains modular code components for processing and analyzing EEG and fNIRS data from the TAFN model.

## Files

1. **Model.py**: Defines a deep learning TAFN model suitable for EEG and fNIRS data.

2. **CustomLoss.py**: Contains a custom loss function for use with the proposed TAFN model.

3. **Data_Augmentation.py**: Implements data augmentation techniques to enhance EEG and fNIRS data variability.

4. **Features_Extraction_fNIRS.py**: Extracts features from fNIRS data.

5. **Features_Extraction_EEG.py**: Extracts features from EEG data.

6. **SignalFraming.py**: Segments EEG or fNIRS signals into frames based on duration and overlap.

7. **BandPassFiltering.py**: Applies a bandpass filter to EEG data within specified frequency ranges.

---

Ensure that all necessary dependencies are installed to use these modules effectively.

# If you use this code, please cite our article:


# Publicly available datasets used in the article:

Dataset 1 from Shin et al. https://doi.org/10.1038/sdata.2018.3

Dataset link: https://doi.org/10.14279/depositonce-5830.2

Dataset 2 from Shin et al. https://doi.org/10.1109/TNSRE.2016.2628057

Dataset link: https://doc.ml.tu-berlin.de/hBCI/

Additional Dataset 1 from Buccino et al. https://doi.org/10.1371/journal.pone.0146610

Dataset links: http://dx.doi.org/10.6084/m9.figshare.1619640 and http://dx.doi.org/10.6084/m9.figshare.1619641

Additional Dataset 2 from Shin et al. https://doi.org/10.1371/journal.pone.0196359

Dataset link: https://doi.org/10.6084/m9.figshare.5900842.v1

