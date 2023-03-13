### **Assigment 6:**

*Sentiment Analysis sobre reviews.*

Through this work, the aim is to integrate notions and knowledge about NLP seen in the module, as well as in previous ones, to generate a machine learning model. The objective will be to build a classifier that can predict whether a user review is positive or negative (good or bad).
To do this, we will use a dataset belonging to the Yelp platform. It has a network of users who provide opinions on nightspots, cultural spaces, commercial establishments, among others.

Objectives: You must generate a machine learning model that can classify English reviews for the Yelp platform. That is, our model will receive a user review and should be able to determine whether it is positive or negative.

Considerations:

● We do not have a target variable as in real-life problems. Therefore, an extra challenge that arises is how to define a target based on the dataset features.

● Often, when we import a dataset, pandas infers what value it could be, and if it does not find a known value, it puts a default one. Validating that the data types of the features correspond to their intrinsic value after importing is a good practice.

● Do a quick exploration of outliers in the dataset. Create the graphs you consider relevant to understand the nature of the problem.

Evaluation:

To evaluate the models, we will use the following metrics:

● Precision;

● Recall; 

● F1-score;

● Analysis of AUC ROC.
