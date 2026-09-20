from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


def build_svm(C=1.0):
    if C <= 0:
        raise ValueError("C must be positive")

    return Pipeline([
        ("scale", StandardScaler()),
        ("model", SVC(C=C))
    ])