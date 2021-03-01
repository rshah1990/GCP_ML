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

## Ranking Metrics

- **ROC AUC** : calculating the false positive rate and true positive rate for a set of predictions by the model under different thresholds.
<img src="DS images/ROC AUC.PNG" width="400">

- **Precision Recall AUC** : the focus on the minority class makes the Precision-Recall AUC more useful for imbalanced classification problems.
<img src="DS images/PR_Curve.PNG" width="400">

## Probabilistic Metrics

- **LogLoss**: These are useful for problems where we are less interested in incorrect vs. correct class predictions and more interested in the uncertainty the model has in predictions and penalizing those predictions that are wrong but highly confident.
