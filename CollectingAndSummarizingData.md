# Collecting and Summarizing Data

We use sample statistics to make inferences about population parameters.

## Data Collection Methods
1. Personal Interview
1. Telephone Interview
1. Questionaire
1. Direct Observation
1. Web-Based Survey

## Types of Bias
1. Non-Response Bias
1. Response Bias
1. Selection

## Strategies for Collecting Data

### Non-Probability Methods
- Convience Sampling (haphazard): Collecting data from subjects who are easily obtained
- Gathering Volunteers: Collecting data from subjects who volunteer

### Probability Methods
 - Simple Randon Sample: making selections from a population where each subject in the population has an equal chance of being selected.
 - Stratified Random Sample: Divide the population into groups based on characteristics then make simple random samples from each group.
 - Cluster Sample: Where a random cluster of subjects is taken from the population of interest. For instance, if we were to estimate the average salary for faculty members at Penn State - University Park Campus, we could take a simple random sample of departments and find the salary of each faculty member within the sampled department. 

 ## Types of Studies

 1. Observational: A study where a researcher records or observes the observations or measurements without manipulating any variables. These studies show that there may be a relationship but not necessarily a cause and effect relationship

 1. Experimental: A study that involves some random assignment* of a treatment; researchers can draw cause and effect (or causal) conclusions. An experimental study may also be called a scientific study or an experiment.

 ## Variables: 
 1. Variable: A variable is any characteristic, number, or quantity that can be measured, counted, or observed for record.
 1. Response Variable: Variable that about which the researcher is posing the question. May also be called the outcome or the dependent variable.
 1. Explanatory Variable: Variables that serve to explain changes in the response. They may also be called the predictor or independent variables.
 1. Lurking Variable: A variable that is neither the explanatory variable nor the response variable but has a relationship (e.g. may be correlated) with the response and the explanatory variable. It is not considered in the study but could influence the relationship between the variables in the study.
 1. Confounding Variable: A variable that is in the study and is related to the other study variables, thus having an effect on the relationship between these variables.

 ## Principles of Experimental Design
 1. Control: Need to control for effects due to factors other than the ones of primary interest.
 1. Randomization: Subjects should be randomly divided into groups to avoid unintentional selection bias in the groups.
 1. Replication: A sufficient number of subjects should be used to ensure that randomization creates groups that resemble each other closely and to increase the chances of detecting differences among the treatments when such differences actually exist.

 ## Classifying Data

 ### Qualitative (Categorical)
 1. Binary: where there are two choices, e.g. Male and Female
 1. Ordinal: where the names imply levels with hierarchy or order of preference, e.g. level of education
 1. Nominal: where no hierarchy is implied, e.g. political party affiliation.

 ### Quantitative
 1. Discrete: or “counted” as in the number of people in attendance
 1. Continuous: or “measured” as in the weight or height of a person.

 #### Proportion: A proportion is a fraction or part of the total that possesses a certain characteristic.

 The best way to summarize categorical data is to use frequencies and percentages like in the table.

 |Eye Color|Freq|%|
 |---|---|---|
 |Brown|24|80%
 |Blue|3|10%|

 ### Graphing Qualitative Variables
 1. Pie Chart
 1. Bar Chart

 ### In MiniTab: Graph -> Pie or Bar Chart

## Measure of Central Tendency
1. Mean: The mean is the average of data.
$$\bar{x} = \Sigma_{i=1}^{n}\frac{x_i}{n} = \frac{1}{n}\Sigma_{i=1}^n x_i$$
1. Median: The median is the middle value of the ordered data.
    - First order the data
    - Find the location of the median by
    - If the median is in between take the mean of the 2 numbers
$$\frac{n+1}{2}$$
    
1. Mode: The mode is the value that occurs most often in the data. It is important to note that there may be more than one mode in the dataset.

## Effect of Outliers


One shortcoming of the mean is that means are easily affected by extreme values. Measures that are not that affected by extreme values are called resistant. Measures that are affected by extreme values are called sensitive.

## Shape
1. Symetrical - mean, median and mode are the same
1. Skewed Left - mean < median (long tail on left)
1. Skewed Right - mean > median (long tail on right)

Use Median with skewed shapes. Since median is not affected much by extereme values.

## Measure of Position
### Finding Quartiles
The data is sorted use. And average if between 2. Q2 is also the median value.
$$Q1 = \frac{n+1}{4}$$
$$Q2 = \frac{2(n+1)}{4}$$
$$Q3 = \frac{3(n+1)}{4}$$

## Measure of Variability

### Range
$$Range = Max - Min$$

### Interquartile Range (IQR)
$$IQR = Q3 -Q1$$

### Variance and Standard Deviation
The standard deviation is the square root of the variance

Variance: the average squared distance from the mean. In the calculations remember to find the mean first if need be.

### Population Variance
$$\sigma^2= \frac{\Sigma_{i=1}^n(x_i - \mu)^2}{N}$$
### Sample Variance
$$s^2=\frac{\Sigma_{i=1}^n(x_i - \bar{x})^2}{n - 1}$$
When we calculate the sample sd we estimate the population mean with the sample mean, and dividing by (n-1) rather than n which gives it a special property that we call an "unbiased estimator". Therefore is an unbiased estimator for the population variance.

Standard Deviation: approximately the average distance the values of a data set are from the mean or the square root of the variance

### Population Standard Deviation
$$\sigma = \sqrt{\sigma^2}$$

### Sample Standard Deviation
$$s = \sqrt{s^2}$$

A rough estimate of SD can be found using $s \approx \frac{Range}{4} $

### Coefficent of Variation
$$CV = \frac{SD}{\mu}$$
To demonstrate, think of prices for luxury and budget hotels. Which do you think would have the higher average cost per night? Which would have the greater standard deviation? The CV would allow you to compare this dispersion in costs in relative terms by accounting for the fact that the luxury hotels would have a greater mean and standard deviation. 

### Graphing One Quantitive Variable
1. DotPlot
1. Stem-and-leaf Diagram
1. Histogram
1. Boxplot

### Potential Outliers
- Lower Limit = Q1 - 1.5 * IQR
- Upper Limit = Q1 + 1.5 * IQR