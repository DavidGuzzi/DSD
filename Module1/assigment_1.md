#### **Assignment 1:**

The objective of the practical work is to carry out a complete Data Exploration on dataset *"data-ecomm-10-19-smallsampled.parquet"*. This exploration involves:

1.	Understanding the domain of the dataset. To do this, ask relevant business questions, such as: Can a user make purchases without first accessing the product or adding it to the cart? Are there products that are purchased more than once by the same user? How many users abandon the cart? And others alike. The focus is to understand the business as much as possible.

2.	Data cleaning. Involves taking actions on all columns of: 
  
  a.	Review, deletion, or imputation of null data; 
  
  b.	Analysis of "unclear" nulls (undefined? zeros?); 
  
  c.	Evaluation of outlier data and analysis of it to decide what action to take; 
  
  d.	Transformation of dates, strings to numeric and/or categorical, and others, if necessary; 
  
  e.	Cleaning of duplicate data; 
  
  f.	Elimination of unnecessary data.
  
  3.	Analysis of univariate distribution of columns.

4.	Analysis of correlation and multi-variable distribution.

5.	Development of a dataset treatment process (suppose a new dataset arrives, the process should perform the same processing done by you to obtain a clean and neat dataset). This can be in a notebook or, ideally, in clean code (.py).

**Valued options.** 

6.  Construction of new columns, linking other columns.

7.	Construction of valuable information columns. For example, day of the week, view rate on purchases for the acquired product, etc.

8.	Ideally, build a target column assuming a purchase prediction. For this, a purchase should be taken as a user who viewed a product -> added it to the cart -> purchased it in the same given time.

9.	In case of building such a column, evaluate the balance (proportion of 1 vs proportion of 0) of it, and the distribution of other variables against the target.

10.	Selection of relevant variables for predicting purchases.
