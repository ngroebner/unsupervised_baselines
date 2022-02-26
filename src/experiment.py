# Experiment base class

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.manifold import TSNE
from .evaluate import evaluate

class Experiment():

    def __init__(
        self,
        dataset,
        preprocessors,
        cluster_algorithm,
        mlflow_url=None
    ):
        """Docstring here"""

        assert type(preprocessors) == list, "Must pass a list of preprocessors"

        self.dataset = dataset
        self.preprocessors = preprocessors
        self.cluster_algorithm = cluster_algorithm
        self._mlflow_url = mlflow_url
        self.predicted_labels = None

        steps = [(p.parameters["name"], p) for p in preprocessors]
        steps = steps + [
            (
                self.cluster_algorithm.parameters["name"],
                self.cluster_algorithm
            )
        ]
        self.pipeline = Pipeline(steps = steps)

        # Create parameter dict
        """self.parameters = dict()
        for k, v in self.dataset.parameters:
            new_k = "dataset_" + k
            self.parameters[new_k] = v
        for k, v in self.preprocessor.parameters:
            new_k = "preprocessor_" + k
            self.parameters[new_k] = v
        for k, v in self.preprocessor.cluster_algorithm:
            new_k = "cluster_" + k
            self.parameters[new_k] = v"""

        # create pipeline

    def saveparams_to_mlflow(self):
        #log the parameters from self.parameters to mlflow db
        raise NotImplementedError

    def fit(self):
        self.pipeline.fit(self.dataset.waveforms, self.dataset.labels)
        return self

    def predict(self):
        # run the experiment, return evaluation metrics
        self.predicted_labels = self.pipeline.predict(self.dataset.waveforms)
        return self.predicted_labels

    def evaluate(self):
        if type(self.predicted_labels) == None:
            print("Must run predict first.")
        else:
            self.confusion_matrix = confusion_matrix(
                self.dataset.labels,
                self.predicted_labels
            )
            metrics = evaluate(self.dataset, self.predicted_labels)
            self.metrics = pd.DataFrame(
                index=metrics.keys(),
                data=metrics.values(),
                columns=["Results"]
            )
            return self.metrics

    def plot_confusion(self, *args, **kwargs):
        disp = ConfusionMatrixDisplay(self.confusion_matrix)
        disp.plot(*args, **kwargs)
        plt.show()
        return disp

    def plot_tsne(self, *args, **kwargs):
        """Scatter plots of transformed data in tsne space.
        Colored by true and predicted labels
        """
        # this retransforms the data slower, but saves memory.
        # could save transformed dataset in the future
        ts = TSNE(*args, **kwargs).fit_transform(self.pipeline.transform(self.dataset.waveforms))
        f, axes = plt.subplots(1,2, figsize=(10,5))
        axes[0].scatter(ts.T[0], ts.T[1], s=1, c=self.dataset.labels)
        axes[0].set_title("True labels")
        axes[1].scatter(ts.T[0], ts.T[1], s=1, c=self.predicted_labels)
        axes[1].set_title("Predicted labels")
        plt.show()

        return f






