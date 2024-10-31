# TAFN
Temporal Attention Fusion Network with custom loss function for EEG-fNIRS classification

This study propose a novel temporal attention fusion network (TAFN) with a custom loss function. The TAFN model incorporates attention mechanisms to its long short-term memory and temporal convolutional layers to accurately capture spatial and temporal dependencies in the EEG–fNIRS data. The custom loss function combines class weights and asymmetric loss terms to ensure the precise classification of cognitive and motor intentions, along with addressing class imbalance issues.

# TAFN Dataset Processing Utilities
This repository contains modular code components for processing and analyzing EEG and fNIRS data from the TAFN model.

# Files
Model.py: Defines a deep learning TAFN model suitable for EEG and fNIRS data.

CustomLoss.py: Contains a custom loss function for use with the proposed TAFN model.

Data_Augmentation.py: Implements data augmentation techniques to enhance EEG and fNIRS data variability.

Features_Extraction_fNIRS.py: Extracts features from fNIRS data.

Features_Extraction_EEG.py: Extracts features from EEG data.

SignalFraming.py: Segments EEG or fNIRS signals into frames based on duration and overlap.

BandPassFiltering.py: Applies a bandpass filter to EEG data within specified frequency ranges.

Ensure that all necessary dependencies are installed to use these modules effectively.
