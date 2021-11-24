# NOOB-ENTITY-
IBM PROJECT-HEALTHCARE DISEASE PREDICTION MODEL

![image](https://user-images.githubusercontent.com/83333946/143203975-81d64ebe-c3f1-4101-a4a7-f596eae80e9d.png)


# Machine Learning Algorithms Used:
## Decision Tree Algorithm:
Decision Trees are some of the most used machine learning algorithms. They are used for both classification and Regression. Decision Trees as the name suggests works on a set of decisions derived from the data and its behavior.


![image](https://user-images.githubusercontent.com/83334866/143196618-321426e4-e646-477d-ae8c-5ab3de4a8ee3.png)

The decision trees use the CART algorithm (Classification and Regression Trees). In both cases, decisions are based on conditions on any of the features. The internal nodes represent the conditions and the leaf nodes represent the decision based on the conditions.


![image](https://user-images.githubusercontent.com/83334866/143196697-08e259c2-2f67-469e-99e8-3ee26455c436.png)


A decision tree is a graphical representation of all possible solutions to a decision based on certain conditions.
On each step or node of a decision tree, used for classification, we try to form a condition on the features to separate all the labels or classes contained in the dataset to the fullest purity.


## Random Forest :
Random forest, like its name implies, consists of a large number of individual decision trees that operate as an ensemble.
Each individual tree in the random forest spits out a class prediction and the class with the 
most votes becomes our model’s prediction (see figure below).

![image](https://user-images.githubusercontent.com/48887731/143194427-43aa4134-5616-4819-b97d-f6ae1497a076.png)

The fundamental concept behind random forest is a simple but powerful one — the wisdom of crowds. In data science speak,
the reason that the random forest model works so well is:
>A large number of relatively uncorrelated models (trees) operating as a committee will outperform any of the individual constituent models.
=======



## Naive Bayes  :
![image](https://user-images.githubusercontent.com/83333946/143196439-05a4a597-2003-47f9-b923-9944018959ee.png)
A Naive Bayes classifier is a probabilistic machine learning model that’s used for classification task. The crux of the classifier is based on the Bayes theorem.

![image](https://user-images.githubusercontent.com/83333946/143196612-4dd44a44-28ab-45a0-8a18-b33c42943232.png)

Using Bayes theorem, we can find the probability of A happening, given that B has occurred. Here, B is the evidence and A is the hypothesis. The assumption made here is that the predictors/features are independent. That is presence of one particular feature does not affect the other. Hence it is called naive.

It is mainly used in text classification that includes a high-dimensional training dataset.
It is a probabilistic classifier, which means it predicts on the basis of the probability of an object.

Some popular examples of Naïve Bayes Algorithm are spam filtration, Sentimental analysis, and classifying articles.

**Working of Naïve Bayes' Classifier:**

1.Convert the given dataset into frequency tables.

2.Generate Likelihood table by finding the probabilities of given features.



3.Now, use Bayes theorem to calculate the posterior probability.

**Python Implementation of the Naïve Bayes algorithm:**

**Steps to implement:**

  1.Data Pre-processing step
  
  2.Fitting Naive Bayes to the Training set
  
  3.Predicting the test result
  
  4.Test accuracy of the result(Creation of Confusion matrix)
  
  5.Visualizing the test set result.

## K-Nearest Neighbor Algorithm:

 K-Nearest Neighbour is one of the simplest Machine Learning algorithms based on Supervised Learning technique.K-NN algorithm assumes the similarity between the new case/data and available cases and put the new case into the category that is most similar to the available categories.K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then it can be easily classified into a well suite category by using K- NN algorithm.
 ![image](https://user-images.githubusercontent.com/94900940/143205649-fba12dd3-1b4e-498c-b011-808efee682f5.png)

 
**The K-NN working can be explained on the basis of the below algorithm:**

1: Select the number K of the neighbors
2: Calculate the Euclidean distance of K number of neighbors
3: Take the K nearest neighbors as per the calculated Euclidean distance.
4: Among these k neighbors, count the number of the data points in each category.
5: Assign the new data points to that category for which the number of the neighbor is maximum.
6: Model is ready.

