# Confidence Intervals

### Two types of Statistical Inference
|Name|Definition|
|---|---|
|Statistical Inference|The real power of statistics comes from applying the concepts of probability to situations where you have data but not necessarily the whole population. The results, called statistical inference, give you probability statements about the population of interest based on that set of data.|
|Estimation|Use information from the sample to estimate (or predict) the parameter of interest.|
|Statistical Tests|Use information from the sample to determine whether a certain statement about the parameter of interest is true. Statistical tests are also referred to as hypothesis tests.|
|Point Estimate|An estimate for a parameter that is one numerical value. An example of a point estimate is the sample mean or the sample proportion.|
|Interval Estimate|Interval estimates give an interval as the estimate for a parameter. |
|Confidence Interval|An interval of values computed from sample data that is likely to cover the true parameter of interest.|
|Precision|The wider the interval, the poorer the precision. Note that the higher the confidence level, the wider the width (or equivalently, half width) of the interval and thus the poorer the precision.|
|Normal Probability Plot|The Normal Probability Plot is a graph that allows us to assess whether or not the data comes from a normal distribution.|

## Types of Statistical Inference

1. Estimation
    1. Point Estimates
    1. Interval Estimates (Confidence Interval)
1. Statistical Tests

## Properties of Good Estimators
1. The center of the sampling distribution for the estimate is the same as that of the population. When this property is true, the estimate is said to be unbiased. The most often-used measure of the center is the mean.

1. The estimate has the smallest standard error when compared to other estimators. 

## Confidence Interval

sample statistic $\pm$ margin of error

The margin of error will consist of two pieces. One is the standard error of the sample statistic. The other is some multiplier, , of this standard error

"We are 'some level of percent confident' that the 'population of interest' is from 'lower bound to upper bound'.

## Inference for Population Proportion


Point estimate of the population proportion

$$\hat{p}=\frac{successes}{n}$$

If....

$np > 5$ and $n(1-p)>5$

Then.... 

$\hat{p}$ is normal with mean $p$ and standard error $\sqrt{\frac{p(1-p)}{n}}$

The multiplier used in the confidence interval will come from the Standard Normal distribution.

But.... 

$p$ is not know. So we use $\hat{p}$

$n\hat{p} > 5$ and $n(1-\hat{p}) > 5$


### Constructing a Confidence Interval

$$\text{point estimate }\pm M\times \hat{SE}(\text{estimate})$$

$$\hat{SE}(\hat{p})=\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

$$\hat{p}\pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$$

where $z_{\alpha/2}$ represents a z-value with $\alpha/2$ area to the right of it.

### Commonly used Alpha levels

|Confidence Level|$\boldsymbol{\alpha}$|$\boldsymbol{z_{\alpha/2}}$|Multiplier|
|---|---|---|---|
|90%|.10|$z_{0.05}$|1.645|
95%|.05|$z_{0.025}$|1.960|
|98%|.02|$z_{0.01}$|2.326|
|99%|.01|$z_{0.005}$|2.576|

### Recall that the margin of error, E, is half of the width of the confidence interval. Therefore for a one sample proportion,

$$E=z_{\alpha/2}\sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$$

The wider the interval, the poorer the precision. Note that the higher the confidence level, the wider the width (or equivalently, half width) of the interval and thus the poorer the precision.


If we want the margin of error smaller (i.e., narrower intervals), we can increase the sample size. Or, if you calculate a 90% confidence interval instead of a 95% confidence interval, the margin of error will also be smaller. 

### Determine Required Sample Size

1. Educated Guess

$$n=\dfrac{z^2_{\alpha/2}\hat{p}_g(1-\hat{p}_g)}{E^2}$$

Where $\hat{p}_g$ is an educated guess for the parameter $p$

*The educated guess method is used if it is relatively inexpensive to sample more elements when needed.*

2. Conservative Method

$$n=\dfrac{z^2_{\alpha/2}(\frac{1}{2})^2}{E^2}$$

*The conservative method is used if the start-up cost of sampling is expensive and thus it is not economical to sample more elements later.*

*Round up and remember if the response rate is not 100% you have to account for that and adjust for the expected.*

## Inference for a Population Mean

The point estimate of the population mean is the sample mean $\bar{x}$.

Remember the following equation from previous lessons. When the population is normal or when the sample size is large then,

$$Z=\dfrac{\bar{x}-\mu}{\dfrac{\sigma}{\sqrt{n}}}$$

where Z has a standard Normal distribution.

But when you don't know the population standard deviation and you replace it with the sample standard error, you no longer have a Z-distribution, you have a t-distribution.

$$t=\dfrac{\bar{X}-\mu}{\dfrac{s}{\sqrt{n}}}$$

### Step #1: Check for conditions...
1. If the sample comes from a Normal distribution, then the sample mean will also be normal. In this case, $\dfrac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}}$ will follow a $t$-distribution with $n-1$ degrees of freedom.

1. If the sample does not come from a normal distribution but the sample size is large ($n \ge 30$), we can apply the Central Limit Theorem and state that $\bar{X}$ is approximately normal. Therefore, $\dfrac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}}$ will follow a -distribution with $n-1$ degrees of freedom.

### Step #2: Construct the General Form
$(1-\alpha)$ 100% Confidence Interval for the Population Mean $\mu$ ,

$$\bar{x}\pm t_{\alpha/2}\dfrac{s}{\sqrt{n}}$$

where the t-distribution has $df = n - 1$
. This interval is also known as the one-sample t-interval for the population mean.

### Step #3: Interpret the Confidence Interval

We are $(1-\alpha)100\%$
confident that the population mean, $\mu$ , is between $\bar{x}-t_{\alpha/2}\frac{s}{\sqrt{n}}$ and $\bar{x}+t_{\alpha/2}\frac{s}{\sqrt{n}}$ .


### If the sample size is less than 30...
Use a normal probability plot to check whether the assumption that the data come from a normal distribution is valid. Do so using Minitab.

### t-distribution
The t-distribution is symmetric about 0, more variable than the Standard Normal Distribution, the larger n get then the closer the t-dist gets to z-dist.

*When the corresponding degree of freedom is not given in the table, you can use the value for the closest degree of freedom that is smaller than the given one. We use this approach since it is better to err in a conservative manner.*

### Minitab
Calc -> Prob Dist -> t
Inverse Cumulative Probability
DoF
Input Constant as 0.95(1-.05)

### Normal Probability Plot
If the sample size is less than 30, one needs to use a Normal Probability Plot. 

Minitab: Graph -> Probabiity Plot

Since the points all fall within the confidence limits, it is reasonable to suggest that the data come from a normal distribution.

### Sample Size Computation for the Population Mean Confidence Interval

$$n=\left(\dfrac{z_{\alpha/2}\sigma}{E}\right)^2$$

### Estimate Std Dev From Range (From Lesson 1)

std dev = range / 4
