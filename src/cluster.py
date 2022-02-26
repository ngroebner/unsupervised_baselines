
class ClusteringMethod:

    def __init__(self, *args, **kwargs):
        """Abstract base class for clustering methods

        Arguments:
            parameters: dict, dictionary of hyperparameter
                names and values for the method
            *args, **kwargs
        """
        self.parameters = None
        raise NotImplementedError

    def fit(self, X, y=None):
        """Fit clustering method to the data if needed.
        If no fitting necessary, leave this as is.
        """
        return self

    def predict(self, X, y=None):
        """Take waveforms and return cluster assignments
        Can do whatever it needs in between to get there.
        """
        raise NotImplementedError

    def save(self, path):
        """Save trained model parameters"""
        raise NotImplementedError