
class Dataset:
    """Abstract base class for a dataset"""

    def __init__(self, *args, **kwargs):
        self.dataset_name = None
        # load dataset

        self.waveforms = None
        self.labels = None