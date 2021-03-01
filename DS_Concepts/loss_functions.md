# Regression Loss Functions

1) **Mean Squared Error Loss**
  - MSE, loss is the default loss to use for regression problems
  - it is the preferred loss function under the inference framework of maximum likelihood if the distribution of the target variable is Gaussian
  - calculated as the average of the squared differences between the predicted and actual values
  - The squaring means that larger mistakes result in more error than smaller mistakes, meaning that the model is punished for making larger mistakes

2) **Mean Squared Logarithmic Error**
  - There may be regression problems in which the target value has a spread of values and when predicting a large value, you may not want to punish a model as heavily as mean squared error.
  - first calculate the natural logarithm of each of the predicted values, then calculate the mean squared error
  - it may be more appropriate when the model is predicting unscaled quantities directly

3) **Mean Absolute Error**:
  - calculated as the average of the absolute difference between the actual and predicted values.
  - loss is an appropriate loss function in this case as it is more robust to outliers

# Binary Classification Loss Functions

1) **Binary Cross-Entropy**
  - It is intended for use with binary classification where the target values are in the set {0, 1}.
  - it is the preferred loss function
  - calculate a score that summarizes the average difference between the actual and predicted probability distributions for predicting class 1.
  - The score is minimized and a perfect cross-entropy value is 0.
  - Formula : - (ylogp + (1-y) log(1-p))

2) **Hinge Loss**
  - primarily developed for use with Support Vector Machine (SVM) models
  - It is intended for use with binary classification where the target values are in the set {-1, 1}.
  - The hinge loss function encourages examples to have the correct sign, assigning more error when there is a difference in the sign between the actual and predicted class values

# Multi-Class Classification

1) **categorical crossentropy**
  - its similar to binary cross entropy but a separate loss for each class label per observation and sum the result.
  - In this target variable must be one-hot encoded
  
![category_crossentropy](https://user-images.githubusercontent.com/37735152/109477250-d19b4480-7a9d-11eb-97c6-633438f581e2.PNG)

2) **Sparse Multiclass Cross-Entropy**
  - when there is large amount of classes one hot encoding can take too much space ex: predicting words in a vocabulary
  -  Sparse cross-entropy addresses this by performing the same cross-entropy calculation of error, without requiring that the target variable be one hot encoded prior to training.
  - sparse_categorical_crossentropy






