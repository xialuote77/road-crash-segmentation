# Reconstruction and checks

Historical source mismatch is resolved by separating provenance, not by rewriting old metrics. Incomplete team source is archived as text; the working entry point is src/cluster_profiles.py. Historical results remain labelled unreconciled and are not used in current findings.

Recomputed on the full supplied cleaned CSV with Python 3.13, scikit-learn 1.8.0, random_state=42 and n_init=10. Three runs checked K=3,4,5; silhouette uses the same seeded sample of 5,000 rows. The input has 400,863 rows. All output profile rows sum to 100% within floating-point tolerance; output counts sum to the input size. No rows were dropped or imputed by the reconstruction.

The input SHA-256 is de00a87b7ed9a3a101d7f350053a720bc6c7e72eba2a7ada1b33e6793a1efe37. This identifies the local input without redistributing it.

A full stability assessment across seeds/bootstrap samples was not performed. Data cleaning is inherited from the team and has not been independently audited. Standardising one-hot columns may over-weight rare categories. Saved groups are exploratory rather than operational personas or causal risk factors.


## Historical communication materials

The original report and slides are now linked under reports/ for communication evidence. The report public copy adds a provenance cover and removes the original first-page author/contact block. Pages 2-14 retain text identical to the original. The 21-slide presentation is copied unchanged. These retain original unsupported or conflicting historical interpretations, explicitly marked in reports/README.md. The slides also contain an incorrect verbal silhouette formula. Current reconstructed evidence takes precedence.
