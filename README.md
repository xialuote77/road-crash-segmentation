# Road-Crash Segmentation: Reproducible Portfolio Reconstruction

## 中文概览

**项目定位：探索性分群 / 行为画像 / 分析复核。** 根据安全带状态、座位和车辆类别进行聚类，再单独比较各组伤害严重程度。

- **个人贡献**：原团队项目中负责聚类模块，以及报告、presentation 中的聚类部分；不包含团队数据预处理和监督分类模块。
- **整理后的复核**：针对历史代码、报告和 CSV 版本不一致的问题，单独补齐运行入口，在 **400,863 行**清洗数据上重跑 K=3/4/5，并保留新旧结果的清楚区分。
- **方法**：one-hot 编码、标准化、KMeans、固定随机种子及 5,000 行样本的 silhouette 比较；伤害严重程度只用于事后画像，不进入聚类。
- **结论边界**：当前分组主要反映车辆类别；“Other/Unknown”占比高的群体首先提示数据解释问题，不能直接包装成可靠业务客群或因果风险因素。当前重构不追认原报告中冲突的结论。

## English documentation

Explore road-user groups using belt status, seating position and vehicle type, then describe injury-severity distributions separately. This portfolio separates an inconsistent historical coursework snapshot from a new, reproducible reconstruction.

## My contribution

I owned the original clustering module and the clustering sections of the team report and presentation. Preprocessing and supervised modelling were team work. The new entry point is a portfolio reconstruction of the stated method, not a claim that the old submission ran unchanged. See [contributions](docs/CONTRIBUTIONS.md).

## Recomputed evidence

The reconstruction was executed on **400,863 rows** of the supplied team-cleaned dataset. Only the three categorical predictors enter the clustering; injury severity is used for post-hoc profiles. One-hot encoded predictors are standardised, with KMeans random_state=42, n_init=10 and a seeded 5,000-row silhouette sample.

| K | Sampled silhouette | Smallest group | Largest group |
| --- | ---: | ---: | ---: |
| 3 | 0.4272 | 29,451 | 80.92% |
| 4 | 0.4675 | 7,221 | 80.13% |
| 5 | 0.5266 | 797 | 73.86% |

At K=3 the group sizes are 29,451 (7.35%), 47,037 (11.73%) and 324,375 (80.92%). The first is predominantly Other/Unknown vehicle types (99.35%), the second is entirely Light Commercial, and the largest is mostly cars (89.01%). These are feature-defined groups, not independently validated risk segments. The Other/Unknown group is especially a data-quality/interpretability concern rather than a business persona.

K=5 has the highest sampled silhouette among the three checked values but a much smaller minimum group. Silhouette alone does not establish an operationally useful segmentation. K=3 is shown as an interpretable example, not claimed as the optimal K. Category scaling, sample sensitivity and cluster stability require further study before operational use. Cluster numbering is arbitrary.

## Run

```bash
python -m pip install -r requirements.txt
python src/cluster_profiles.py --input /path/to/cleaned_data.csv --output results/new-run --k 3
```

The input requires complete columns HELMET_BELT_WORN_STATUS, SEAT_CATEGORY, VEHICLE_TYPE and SEVERITY_CATEGORY. Raw records are not bundled. The script exports aggregate profiles and counts, not person-level assignments. Recomputed outputs and the exact validation environment are under results/recomputed/ and docs/REVIEW.md.

## Historical snapshot reconciliation

The original CSV counts described almost all records in one group; another table had five groups while the report described three. The root script had a missing fitting loop, and a second variant had invalid syntax. Those snapshots do not authenticate the report's original claims. Historical tables are labelled under results/unreconciled/, exploratory screenshots under assets/, and the incomplete team source is archived as plain text under docs/archive/ rather than presented as runnable code.

The new results above supersede those snapshots for this portfolio presentation. They do not retroactively validate the submitted report. No causal claim is made about seatbelt use or injury severity.

Originally COMP20008 Assignment 2, University of Melbourne. Team attribution is retained; member contact details, signed contracts, full group report and raw/person-level data are excluded.
