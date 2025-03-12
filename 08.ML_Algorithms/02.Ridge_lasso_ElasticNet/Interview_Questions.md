# Interview Questions on Regularization Techniques 📊

This document contains a set of interview questions and answers based on **Ridge**, **Lasso**, and **Elastic Net** regularization techniques. These are essential concepts in Machine Learning and will help you prepare for related interviews.

---

## 1. What is regularization in machine learning, and why is it important?

**Answer**:  
Regularization is a technique used to prevent overfitting by adding a penalty term to the loss function. It helps reduce the model complexity, forcing it to generalize better on unseen data. Without regularization, models can memorize the training data, leading to poor performance on test data.

---

## 2. Can you explain the difference between Ridge and Lasso regression?

**Answer**:

- **Ridge regression** uses L2 regularization, where the penalty term is the sum of the squared coefficients. It shrinks the coefficients but doesn't set them to zero.
- **Lasso regression** uses L1 regularization, where the penalty term is the sum of the absolute values of the coefficients. It can shrink some coefficients to zero, effectively performing feature selection.

---

## 3. What does L2 regularization (Ridge) do to the coefficients of a linear regression model?

**Answer**:  
L2 regularization (Ridge) shrinks the coefficients toward zero but never completely sets them to zero. It helps reduce the impact of less important features and controls multicollinearity.

---

## 4. How does Lasso (L1 regularization) shrink the coefficients in a regression model?

**Answer**:  
Lasso (L1 regularization) adds a penalty proportional to the absolute value of the coefficients. As the penalty increases, the coefficients are shrunk towards zero, and some coefficients may become exactly zero, which helps in feature selection.

---

## 5. What is the key difference between Ridge, Lasso, and Elastic Net regularization?

**Answer**:

- **Ridge** uses L2 regularization, penalizing the sum of squared coefficients.
- **Lasso** uses L1 regularization, penalizing the sum of absolute coefficients, allowing some coefficients to become zero (feature selection).
- **Elastic Net** is a combination of both L1 and L2 regularization, balancing the advantages of both Ridge and Lasso.

---

## 6. Can you explain the concept of **shrinkage** in regularization?

**Answer**:  
Shrinkage refers to the process of reducing the magnitude of the model coefficients towards zero. Regularization techniques like Ridge and Lasso apply shrinkage to control the size of the coefficients and avoid overfitting.

---

## 7. What is the impact of increasing the regularization parameter (λ) in Ridge regression?

**Answer**:  
Increasing λ in Ridge regression strengthens the penalty term, causing the model to shrink the coefficients more. This can help reduce overfitting but may also introduce bias into the model, leading to underfitting if λ is too large.

---

## 8. In Lasso regression, why do some coefficients become exactly zero?

**Answer**:  
Lasso regression uses L1 regularization, which encourages sparsity in the model. As the penalty term increases, it forces some coefficients to shrink to exactly zero, effectively removing those features from the model and performing feature selection.

---

## 9. How does Elastic Net combine the benefits of both Ridge and Lasso regression?

**Answer**:  
Elastic Net combines L1 and L2 regularization. It retains Lasso’s ability to select features by setting some coefficients to zero, while also incorporating Ridge’s ability to handle multicollinearity and prevent overfitting by shrinking coefficients toward zero without eliminating them.

---

## 10. What is the role of the **α** parameter in Elastic Net?

**Answer**:  
The **α** parameter in Elastic Net controls the balance between L1 and L2 regularization:

- **α = 1** corresponds to Lasso regression (pure L1 regularization).
- **α = 0** corresponds to Ridge regression (pure L2 regularization).
- **0 < α < 1** results in a mix of both L1 and L2 regularization.

---

## 11. How do you choose the optimal value for the regularization parameter λ in Ridge, Lasso, and Elastic Net?

**Answer**:  
The optimal value for λ is usually determined using cross-validation. Techniques like **Grid Search** or **Random Search** are commonly used to find the best λ by testing different values and evaluating model performance on validation data.

---

## 12. Why might Ridge regression perform better than Lasso in datasets with highly correlated features?

**Answer**:  
Ridge regression performs better in cases of multicollinearity because it shrinks the coefficients evenly, whereas Lasso may randomly select one feature from a group of correlated features and set others to zero, potentially discarding important features.

---

## 13. Can Lasso regression be used for feature selection? How?

**Answer**:  
Yes, Lasso regression can be used for feature selection. As Lasso applies L1 regularization, it forces some of the coefficients to exactly zero, effectively removing those features from the model. This results in a more interpretable and sparse model.

---

## 14. When would you prefer Elastic Net over Lasso or Ridge regression?

**Answer**:  
Elastic Net is preferred when there are many correlated features, as it combines both Lasso's feature selection and Ridge’s regularization. It is particularly useful when neither Lasso nor Ridge performs well on their own.

---

## 15. What happens if you set **α = 0** in Elastic Net?

**Answer**:  
Setting **α = 0** in Elastic Net makes the model behave exactly like Ridge regression. It applies only L2 regularization and does not perform feature selection, instead shrinking all coefficients toward zero.

---

## 16. How does Elastic Net handle highly correlated features?

**Answer**:  
Elastic Net handles highly correlated features better than Lasso by allowing some correlation among features while still performing regularization. It uses both L1 and L2 penalties, which helps avoid the problem of selecting one feature from a correlated group (as in Lasso).

---

## 17. Can Ridge regression handle non-linear relationships?

**Answer**:  
Ridge regression, like Lasso, assumes a linear relationship between features and the target variable. If the relationship is non-linear, Ridge regression will not perform well unless additional techniques (like feature transformation) are applied.

---

## 18. What are the advantages of using Lasso over Ridge?

**Answer**:  
Lasso is advantageous when you expect many features to be irrelevant. It helps by performing automatic feature selection, driving some coefficients to zero. Ridge does not perform feature selection and shrinks all coefficients without removing any.

---

## 19. What is the primary disadvantage of Ridge regression?

**Answer**:  
The primary disadvantage of Ridge regression is that it does not perform feature selection. It shrinks all coefficients but keeps them non-zero, making it less interpretable when dealing with high-dimensional data where many features may be irrelevant.

---

## 20. Can you apply Lasso or Ridge regression to non-linear data?

**Answer**:  
Lasso and Ridge are designed for linear relationships. For non-linear data, these techniques would need to be combined with non-linear transformations (e.g., polynomial features) or with non-linear models (e.g., decision trees).

---

## 21. How would you assess the performance of a model using Ridge or Lasso regression?

**Answer**:  
The performance of a model using Ridge or Lasso regression can be assessed using metrics like **Mean Squared Error (MSE)** or **R²**. Cross-validation can be used to evaluate how well the model generalizes to unseen data.

---

## 22. What is the difference between the coefficients of Ridge and Lasso regression after training?

**Answer**:  
In Ridge regression, all coefficients are shrunk but none are exactly zero. In Lasso regression, some coefficients may become exactly zero, effectively removing those features from the model.

---

## 23. What is the effect of λ on the model complexity in Ridge and Lasso?

**Answer**:  
Increasing λ reduces the model's complexity by shrinking the coefficients more, making the model simpler. However, if λ is too large, it may cause underfitting, where the model cannot capture the underlying patterns in the data.

---

## 24. What is the relationship between Ridge regression and Principal Component Regression (PCR)?

**Answer**:  
Ridge regression can be interpreted as performing Principal Component Regression (PCR) with a specific constraint on the eigenvalues. PCR focuses on transforming the features into principal components, while Ridge penalizes large coefficients.

---

## 25. How do Ridge and Lasso regression handle multicollinearity?

**Answer**:

- **Ridge regression** handles multicollinearity well by shrinking the coefficients of correlated features, reducing their impact without eliminating them.
- **Lasso regression** may randomly select one feature from a group of correlated features and set the others to zero, which could be problematic in the case of high correlation.

---

### Summary:

- **Ridge** (L2) shrinks coefficients but doesn't eliminate any features.
- **Lasso** (L1) performs feature selection by setting some coefficients to zero.
- **Elastic Net** combines the strengths of both Ridge and Lasso.

Good luck with your interview preparation! 😊
