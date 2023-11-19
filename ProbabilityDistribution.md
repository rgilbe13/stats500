# Probability Distribution
|Term|Definition|
|---|---|
|Random Variable|A random variable is a variable that takes on different values determined by chance. In other words, it is a numerical quantity that varies at random.|
|Discrete Random variable|When the random variable can assume only a countable, sometimes infinite, number of values.|
|Continuous Random Variable|When the random variable can assume an uncountable number of values in a line interval.|
|Probability Function|A probability function is a mathematical function that provides probabilities for the possible outcomes of the random variable, . It is typically denoted as f(x).|
Probability Mass Function (PMF)|If the random variable is a discrete random variable, the probability function is usually called the probability mass function (PMF)|
|Probability Density Function|If the random variable is a continuous random variable, the probability function is usually called the probability density function (PDF).|
|Cumulative Distribution Function|usually denoted F(x) , is a function that gives the probability that the random variable, X, is less than or equal to the value x.|
## Expected Value of a Discrete Random Variable
The expected value (or mean) of a discrete random variable.
For a discrete random variable, the expected value, usually denoted as $\mu$ or E(X), is calculated using
$$\mu = E(X) = \sum{x_i f(x_i)}$$
The formula means we multiply each value of x by it's respective probability and add them together. 

## Variance of a Discrete Random Variable

$$\sigma^2 = Var(X) = \sum{x^2_i f(x_i) - E(X)^2} = \sum{x^2_i f(x_i)} - \mu^2$$

There is another form of this formula but this is the one we will be using in class. The formula means that first, we sum the square of each value times its probability then subtract the square of the mean. 

## Standard Deviation of a Discrete Random Variable
The standard deviation of a random variable, , is the square root of the variance.

$$\sigma = SD(X) = \sqrt{Var(X)} = \sqrt{\sigma^2}$$

## Binomial Distribution
We have a binomial experiment if ALL of the following four conditions are satisfied:

1. The experiment consists of n identical trials.
1. Each trial results in one of the two outcomes, called success and failure.
1. The probability of success, denoted p, remains the same from trial to trial.
1. The n trials are independent. That is, the outcome of any trial does not affect the outcome of the others.

If the four conditions are satisfied, then the random variable $X$=number of successes in $n$ trials, is a binomial random variable with
$$\mu = E(X) = np$$
$$Var(X) = np(1 - p)$$
$$SD(X) = \sqrt{np(1 - p)}$$

## Binomial Formula
For a binomial random variable with probability of success,$p$ , and $n$ trials...
$$P(X=x) = \frac{n!}{x!(n-x)!}p^x(1-p)^{n-x}$$

## Z-score
The Z-value (or sometimes referred to as Z-score or simply Z) represents the number of standard deviations an observation is from the mean for a set of data. To find the z-score for a particular observation we apply the following formula:
$$Z = \frac{x - \mu}{SD}$$
Where x is the observed value, u is the mean over the standard deviation.
 ## Z-score and Percentile
 The values inside the table represent probability which is also the percentile. Say you want to to find the 10th percentile. Look for .1000 in the table. Work backwards to find the z-score and use the above calculation to find the x value.