# Hypothesis Testing

## Six Step for Hypothesis Testing
### 1. Setup the hypothesis and check for condidtions.

Null Hypothesis: The null hypothesis is typically denoted as $H_0$. The null hypothesis states the "status quo". This hypothesis is assumed to be true until there is evidence to suggest otherwise.

$H_0:p=p_0$ or $H_0:\mu = \mu_0$

The null hypothesis is always equal the status quo value

Alternative Hypothesis: The alternative hypothesis is typically denoted as $H_a$ or $H_1$ . This is the statement that one wants to conclude. It is also called the research hypothesis.
The alt hypothesis can be different greater than or less than the null hypothesis. ie

$p \ne p_0$ OR $p > p_0$ OR $p < p_0$

#### Check conditions 

$$np > 5, n(1-p) > 5$$

*Use the null hypothesis proportions since the null hypothesis is assumed to be true.*

$$np_0 > 5, n(1-p_0) > 5$$

If both greater than five, then the sampling distribution of the sample proportion will be approximately normal with mean $p_0$ and standard error $\sqrt{\frac{p_0(1-p_0)}{n}}$

### 2. Decide on a significance level, $\alpha$:

This value is used as a probability cutoff for making decisions about the null hypothesis. This alpha value represents the probability we are willing to place on our test for making an incorrect decision in regards to rejecting the null hypothesis. The most common $\alpha$ value is 0.05 or 5%. Other popular choices are 0.01 (1%) and 0.1 (10%).

*The level of significance is also the probability of a Type I error*

### 3. Calculate the test statistic

$$z^*=\dfrac{\hat{p}-p_0}{\sqrt{\dfrac{p_0(1-p_0)}{n}}}$$

### 4. Calculate probability value (p-value), or find the rejection region
**P-value**: The p-value (or probability value) is the probability that the test statistic equals the observed value or a more extreme value under the assumption that the null hypothesis is true.

- If our p-value is less than or equal to $\alpha$
, then there is enough evidence to reject the null hypothesis.
- If our p-value is greater than $\alpha$
, there is not enough evidence to reject the null hypothesis.

**Critical Value**: The values that separate the rejection and non-rejection regions.

**Rejection Region**: The set of values for the test statistic that leads to rejection of $H_0$

### 5. Make a decision about the null hypothesis
1. Reject the null hypothesis
1. Fail to reject the null hypothesis


### 6. State an overall conclusion
---
___
## Types of Errors
|||
|---|---|
|Type I Error|When we reject the null hypothesis when the null hypothesis is true.|
|Type II Error|When we fail to reject the null hypothesis when the null hypothesis is false.|
|$\alpha$|The probability of committing a Type I error. Also known as the significance level.|
|$\beta$|The probability of committing a Type II error.|
|Power|Power is the probability the null hypothesis is rejected given that it is false (ie.$1-\beta$ )|