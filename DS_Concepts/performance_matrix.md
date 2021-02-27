# Binary Classification 

- Evaluation metrics can be boradly divided into 3 categories 
  - **Threshold Metrics** : Threshold metrics are those that quantify the classification prediction errors. (Recall, Precision)
  - **Ranking Metrics**: Rank metrics are more concerned with evaluating classifiers based on how effective they are at separating classes. (ROC Curve)
  - **Probability Metrics**: Probabilistic metrics are designed specifically to quantify the uncertainty in a classifier’s predictions. (logloss)


## Threshold Metrics

<img src="DS images/confusion matrix.png" width="400">

**Note: TPR == Recall == Sensitivity**

- **Precision** : summarizes the fraction of examples assigned the positive class that belong to the positive class.

                TruePositive / (TruePositive + FalsePositive)
- **Recall**: summarizes how well the positive class was predicted and is the same calculation as sensitivity.

                TruePositive / (TruePositive + FalseNegative)
- **F-score**: Precision and recall can be combined into a single score that seeks to balance both concerns, called the F-score.

                (2 * Precision * Recall) / (Precision + Recall)
- **Sensitivity** : summarizes how well the positive class was predicted.

                TruePositive / (TruePositive + FalseNegative)

- **Specificity**: summarises how well the negative class was predicted.
 
                TrueNegative / (FalsePositive + TrueNegative)

- **TruePositiveRate** :

                TruePositive / (TruePositive + FalseNegative)
           
- **FalsePositiveRate** :

                FalsePositive / (FalsePositive + TrueNegative)

