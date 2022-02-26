# API for the clustering project

Parts/steps

1. Datasets
    - Combined waveform data as numpy array with labels as integers
    - either pandas dataframe or class like a pytorch dataset
    - yields the waveforms and labels as needed
2. Preprocess
    - Takes a dataset, parameters and yields transformed waveforms
    - Any filtering or other processing applied to the dataset uniformly before clustering
3. Cluster
    - Takes transformed waveforms, parameters and yields predicted cluster assignments
    - May be broken into parts based on model (e.g. create features, calculate distances, do clustering and prediction, etc)
4. Evaluate
    - Takes predicted cluster assignments and true cluster assignments, calculates metrics.
    - Accuracy, nmi, ami, etc
5. Report
    - Takes metrics and produces human readable report

## Pipeline pseduocode

```pseudocode
    for dataset in Datasets:

        Preprocess dataset

        for method in Clustering_Methods:

            for hyperparameters in hyperparameter_choices:

                cluster preprocessed dataset

                evaluate clusters

                save results
```

Report

If we are doing hyperparameter tuning, do we tune based on true cluster labels (seems too contrived) or by some other goodness of fit like silhouette score

## Dataset

Should have a single class that takes the name of a dataset as a string and then loads in the data as waveforms and labels

```python
class Dataset:

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        # load dataset based on name

        self.waveforms = None
        self.labels = None
```

## Preprocess

```python
class Preprocess:
    """Abstract base class for dataset transformer"""

    def __init__(self, mlflow_server, *args, **kwargs):
        self.mlfow_server = mlflow_server
        pass

    def transform(self, dataset):
        # take dataset as an argument and return a transformed dataset
        raise NotImplementedError
```

## Clustering method

```python
class ClusteringMethod:
    """Abstract base class for clustering methods"""

    def __init__(self, mlflow_server, *args, **kwargs):
        self.mlfow_server = mlflow_server
        raise NotImplementedError

    def run(self, dataset):
        """Should take a dataset and return cluster assignments
        Can do whatever it needs in between to get there.
        """
        raise NotImplementedError
```

## Evaluate

```python
def evaluate(dataset, predicted_clusters):
    true_clusters = dataset.labels
    # Calc and return a bunch of metrics here
```
