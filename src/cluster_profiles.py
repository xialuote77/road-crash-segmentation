"""Portfolio reconstruction of the clustering method, not a historical-result reproduction."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

PREDICTORS = ['HELMET_BELT_WORN_STATUS', 'SEAT_CATEGORY', 'VEHICLE_TYPE']

def analyse(frame, k=3, seed=42):
    missing = set(PREDICTORS + ['SEVERITY_CATEGORY']) - set(frame.columns)
    if missing:
        raise ValueError(f'Missing required columns: {sorted(missing)}')
    if frame[PREDICTORS + ['SEVERITY_CATEGORY']].isna().any().any():
        raise ValueError('Input must contain complete preprocessed categories; no silent imputation.')
    encoded = pd.get_dummies(frame[PREDICTORS], drop_first=True, dtype=float)
    if encoded.shape[1] == 0 or k < 2 or k >= len(frame):
        raise ValueError('Need varying categorical features and 2 <= k < row count.')
    features = StandardScaler().fit_transform(encoded)
    labels = KMeans(n_clusters=k, random_state=seed, n_init=10).fit_predict(features)
    if len(np.unique(labels)) != k:
        raise ValueError('Fewer distinct clusters than requested; inspect feature diversity.')
    profiled = frame[PREDICTORS + ['SEVERITY_CATEGORY']].copy()
    profiled['cluster'] = labels
    counts = profiled.groupby('cluster').size().rename('rows').to_frame()
    counts['percent'] = counts['rows'] / len(profiled) * 100
    rng = np.random.default_rng(seed)
    sample = rng.choice(len(frame), size=min(5000, len(frame)), replace=False)
    sampled_labels = labels[sample]
    score = (float(silhouette_score(features[sample], sampled_labels))
             if 1 < len(np.unique(sampled_labels)) < len(sample) else None)
    profiles = {column: pd.crosstab(profiled['cluster'], profiled[column], normalize='index') * 100
                for column in PREDICTORS + ['SEVERITY_CATEGORY']}
    return counts, profiles, score

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('results/recomputed'))
    parser.add_argument('--k', type=int, default=3)
    args = parser.parse_args()
    counts, profiles, score = analyse(pd.read_csv(args.input), args.k)
    args.output.mkdir(parents=True, exist_ok=True)
    counts.to_csv(args.output / 'cluster_counts.csv')
    for column, table in profiles.items():
        table.to_csv(args.output / f'profile_{column.lower()}.csv')
    print(f'Sampled silhouette: {score}; descriptive clustering, not causal risk estimation.')

if __name__ == '__main__':
    main()
