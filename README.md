# Unsupervised algorithm comparison for seismic/acoustic waveforms

Please see the [API documentation](API.md) for details on how the code is set up.

## Goals

1. Compare the performance of multiple clustering algorithms applied to acoustic/seismic waves with known class labels.
2. Understand which methods are most appropriate for clustering seismic and acoustic waves for specific purposes.
3. Understand the clusters produced by each method, i.e., what are the features of the waveforms unique to each cluster?

## Experimental Approach

- Apply several clustering methods (including “traditional” and deep learning methods) to several *labeled* datasets of acoustic events and seismic data. Each dataset should have a set or sets of labels that assign a geologically useful parameter to the waveform. Could be a source parameter, could be a path parameter, etc.
- Waveforms in each dataset will be clustered by each of the chosen algorithms. The “success” of each algorithm will be based on how well the identified clusters match the preassigned labels. Preference should be given to algorithms that have been used previously on geological datasets.
- Investigation of each algorithm’s clusters - what are the unique statistical properties of each cluster produced by each method? Are they similar across datasets? Don’t want to get too bogged down in this one, so I’d suggest just calculating a standard set of statistics (energy, entropy, variance, kurtosis, etc) for each cluster and seeing if any are statistically significantly different.
- Code follows a standard structure [API](API.md) for each model and dataset. This makes analysis of multiple datasets and techniques faster and more efficient.

## Unsupervised methods in the geological literature

|Reference|Time vs freq domain|Feature extraction|Clustering algo|Event or continuous|Setting|
|---------|-------------------|------------------|---------------|-------------------|-------|
|Unsupervised Deep Clustering of Seismic Data: Monitoring the Ross Ice Shelf, Antarctica, Earth and Space Science Open Archive|Frequency -spectrogram|Autoencoder|GMM or DEC|Event|Ross Ice shelf|
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021JB022455|Frequency - wavelet|Scattering transform -> ICA|Hierarchical|continuous|Anatolia|
|Specufex, Holtzman et al 2018|Frequency - spectrogram|NMF -> HMM|K-means|event|The Geysers|
|https://agupubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2020GL088353?casa_token=4Hkq8NEAhu4AAAAA:AMClwkwIp_1CSf4L0KhuNkU-7o8EjzoRpWkhdmzAXILWsqinP-zq2lpqkXKF-gDluEa9sf9s2xhLIN4|Time - waveform|Engineered statistical features|K-means|continuous|ocean|
|https://academic.oup.com/gji/article/182/3/1619/600346|Time - waveform|Engineered statistical features|Self organizing map|continuous|Mt Merapi|
https://ieeexplore.ieee.org/document/8704258|Time- waveform|Autoencoder|DEC|Event|Local vs teleseismic equakes|

## Baseline methods

- L1/L2/correlation/DTW distance between waveforms
- L1/L2/correlation/DTW distance between spectrograms
- L1/L2 distance between spectra (spectra are not shift and warping invariant, so can’t use DTW or correlation)

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can
    |                         be imported.
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    |   ├── cluster.py     <- Abstract base class for clustering methods.
    |   |
    |   ├── dataset.py     <- Abstract base class for datasets.
    |   |
    |   ├── evaluate.py    <- Functions for evaluating the results of a clustering method.
    |   |
    |   ├── experiment.py  <- Abstract base class for encapsulating and experimental run.
    |   |
    |   ├── preprocess.py  <- Abstract base class for a preprocessing method.
--------

