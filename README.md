# StrumSuggest

## Prototype Recommendation Engine for Similar Guitars

This project aims to create a prototype recommendation engine for recommending similar electric guitars to users. The recommendation engine will work by clustering guitars based on their specifications and use that as the basis for the recommendation function. This was a time limited capstone project that was completed in ~7 days so there is much room for improvement.

## Code and Resources Used
**Editors:** 
* for webscraping - Google Collab Python 3.10.11
* everything else - Dataspell 2022.3.1 Python 3.11.2

**Python Packages:** 
* **Data Manipulation:** *pandas* and *numpy* for importing, handling and manipulating data
* **Data Visualisation:** *matplotlib* and *seaborn* for graphing
* **Machine Learning:** *sklearn* for data preprocessing, ML modelling and evaluation

# Project Contents

## Data Gathering
The data for this project was gathered by web scraping from an online guitar store. The data collected includes the brand, model, body shape, number of frets, number of strings, pickup types, price of each guitar along with many other features. The data was then processed and consolidated into a single dataset.

## Exploratory Data Analysis and Feature Selection
After collecting and consolidating the data, exploratory data analysis (EDA) was performed to gain insights into the dataset. The EDA process involved analyzing the distributions of features, looking for correlations between features, and identifying any outliers or missing values.

Based on the results of the EDA, feature selection was performed to identify the most relevant features for clustering and recommendation. The selected features include brand, model, number of frets, radius, price, scale length and bridge type.

## Clustering and Recommendation Models
With the selected features, DBSCAN was implemented and the data was clustered. For DBSCAN 2 hyperparameters must be chosen prior to modelling. These were tuned using a GridSearch approach and 3 models were examined based on the amount of clusters produced and their silhouette scores:
- High no. of clusters (171)
- Medium no. of clusters (63)
- Low no. of clusters (18)

These were then used as the basis for the Recommendation function. The function takes in a users' electric guitar model name and outputs the name and specs of the most similar one. A model is in the same cluster as the input, and with the shortest Euclidean Distance from the input model, is chosen as the most similar. The function also outputs the furthest model in the cluster as a variation suggestion.

## Conclusion
While the project successfully achieved its aim of creating a prototype recommendation engine for recommending similar guitars to users, there are still several areas that could be improved upon. Specifically, better data acquisition methods, as well as a more thorough exploration of the gathered data and the features used in the modelling process could greatly improve the final model.

Other methods of assessing the performance of the models, alternative clustering algorithms and overall limitations are also briefly discussed in this section.







