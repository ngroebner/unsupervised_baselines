
class Preprocessor:
    """Abstract base class for dataset transformer.
    Designed to work with scikit-learn Pipeline class"""

    def __init__(self):
        """Do any setup needed here, eg save hyperparameters """
        raise NotImplementedError

    def fit(self, X=None, y=None):
        """If the preprocessor needs to be fit on the data,
        do that here. Otherwise don't change this.
        """
        return self

    def transform(self, X, y=None):
        """Take waveforms as an argument and return a transformed dataset
        do something to the dataset like filter waveform,
        create spectrogram, etc
        """

        raise NotImplementedError