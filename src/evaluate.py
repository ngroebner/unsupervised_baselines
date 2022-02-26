# function(s) for evaluating clustering methods

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    normalized_mutual_info_score as nmi,
    adjusted_rand_score as ari,
    accuracy_score as acc,
    homogeneity_completeness_v_measure as hcv
)

def evaluate(dataset, predicted_labels):
    """Calculate standard clustering metrics

    Arguments:
        dataset: Dataset class, the dataset containing the true cluster labels

    Returns:
        dict
            _ari_: adjusted Rand score
            _nmi_: normalized mutual information
            _acc_: accuracy
            _hom_: homogeneity
            _compl_: completeness
            _v_: v-measure

            See [Sckit-learn's clustering documentation]
            (https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation)
             for further details
    """

    true_labels = dataset.labels

    results = {}
    results["ari"] = ari(true_labels, predicted_labels)
    results["nmi"] = nmi(true_labels, predicted_labels)
    results["acc"] = acc(true_labels, predicted_labels)
    hom, compl, v = hcv(true_labels, predicted_labels)
    results["homogeneity"] = hom
    results["completeness"] = compl
    results["v"] = v

    return results

