# Road-Crash Segmentation: Reproducible Portfolio Reconstruction

## 中文概览

### 道路事故中的道路使用者分群

根据安全带使用状态、座位和车辆类别识别道路使用者群体，再比较各组的伤害严重程度，探索不同特征组合对应的事故记录分布。

- **个人工作**：负责原团队项目的聚类模块，以及报告和课堂展示中的聚类部分。数据预处理与监督分类由团队协作完成。
- **分析方法**：对类别变量进行独热编码和标准化后使用 KMeans 聚类；比较 K=3、4、5，并在固定的 5,000 行样本上计算轮廓系数。伤害严重程度仅用于聚类后的群体描述。
- **复核结果**：整理版在 **400,863 条**清洗记录上重新运行。K=3 时，三个群体分别占 7.35%、11.73% 和 80.92%；分组主要反映车辆类别，未知类别也提示了数据解释上的局限。

当前代码是对原方法的重构。历史代码、报告和结果表存在版本差异，仓库分别保留原课程材料与重跑结果。分群用于描述数据中的特征组合，不能直接证明因果风险或支持干预决策。

## 报告与展示

- [课程报告（公开副本）](reports/historical-team-report.pdf)：保留原报告，移除学号和邮箱，并补充材料说明。
- [原团队展示（21 页 PPTX）](reports/historical-team-slides.pptx)：包含本人负责的聚类部分及其他团队内容。

历史材料与当前重跑结果的差异见[材料说明](reports/README.md)。当前结果见下方分析和 `results/recomputed/`。

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

Originally COMP20008 Assignment 2, University of Melbourne. Team attribution is retained; member contact details, signed contracts and raw/person-level data are excluded. A public copy of the historical full team report and original presentation is retained under [reports/](reports/README.md), with explicit provenance and reconciliation notes.
