# Historical report and presentation

- [Full team report, public copy](historical-team-report.pdf): original 14 report pages plus a provenance/review cover. The first-page author/contact block was removed to exclude student numbers and university email addresses. All later report pages are preserved.
- [Original team presentation](historical-team-slides.pptx): original 21-slide PPTX, unchanged. It includes team context beyond the clustering sections contributed by Kunze (Charlotte) Lyu.

These are historical coursework materials, not the current reconstructed analysis. Cluster counts, vehicle profiles and silhouette claims differ across the old report, slides, source and CSVs. The presentation itself notes that the historically quoted k=3 silhouette of 0.83 was not recovered in later samples. The portfolio reconstruction measures 0.4272 at k=3, 0.4675 at k=4 and 0.5266 at k=5 on the stated sample and input.

Read the current repository README, results/recomputed/ and docs/REVIEW.md for supported results. Old risk labels and policy/causal interpretations are not validated by clustering alone. The slides' “cohesion minus separation” silhouette wording is also inconsistent with the standard sign convention, which is (b-a)/max(a,b), where a is within-cluster dissimilarity and b is nearest-other-cluster dissimilarity. It is retained as an original historical error, not endorsed.

Team: Tianrui Chen, Xinping Ouyang, Kunze (Charlotte) Lyu and Na Yu. Personal contribution: clustering implementation and the clustering sections of the report and presentation. Other modules remain team work. No licence is assigned to team materials.
