# AI platform- Model explanation

- Explanation (feature attribution) for each and every prediction helps you to understand model output for classification and regression
- Available for tabular data as well as image data 
- **Limitation: only supports model trained on TensorFlow 1.x if you are using keras than have to convert into estimators using model to estimator utility** 
  - tf.keras.estimator.model_to_estimator(keras_model=estimator_model)
  
# Methods

- AI explanation offers two method. **Both methods are based on concept of SHAP values**.
- - XRAI -> images (XRAI is based on Integrated Gradients and also can’t be used on non-differentiable models)
  - Integrated gradients -> everything else that’s differentiable. 
  - Sampled Shapley -> only for ensembles and other non-differentiable models

## Sampled shapely
- For non-differentiable models such as ensemble models of tree
## Integrated gradients
- most suitable for differential models like deep neural network 
- especially useful for model having large feature space
- it computes gradients of an output with respect to input. Multiplied element wise with input itself (Taylor approximation of predicted function at input)
## XRAI
- XRAI combines integrated gradients method with additional steps to determine which region of image contribute to the class prediction rather than pixel level.
- Original image -> ( over-segment Image + Pixel-based attribution (Integrated gradients)) -> sum attributions & identify important region -> most important region for predicted class
