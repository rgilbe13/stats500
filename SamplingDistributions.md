# Sampling Distributions
### Statistic: Characteristic of a sample.

| Characteristic | Notation |
|---|---|
| Sample Mean | $\bar{x}_1, \bar{x}_2, \bar{x}_3, \bar{x}_n $ |
|Sample Proportion| $\hat{p}$
|*Standard Error| $SE(\bar{X}$)|

    *Same as standard deviation but for a statistic it is called standard error.



### Parameter: Characteristic of a population.
| Characteristic | Notation |
|---|---|
|Population Mean| $\mu$
|Population Standard Deviation| $\sigma$|
|Population Proportion| $p$ or $\pi$|

#### Sampling Distribution: The sampling distribution of a statistic is a probability distribution based on a large number of samples of size from a given population.

#### Sampling Error: The error resulting from using a sample characteristic to estimate a population characteristic. 

| Characteristic | Notation |
|---|---|
|Mean of the Sample Means| $\mu_{\bar{x}}$

#### Mean of the Sample Mean
$$\mu_{\bar{x}} = \sum \bar{x}_i f(\bar{x}_i) = 10(\frac{1}{3}) + 12(\frac{1}{3}) + 14(\frac{1}{3})$$

### Z-Score of a Sample Mean
$$z = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}}$$

Example where to use z-score: what is the probability that the sample mean will be....
1. Find the z-score
1. Use the chart to look at the probability

### Central Limit Theorem
The sample mean is normally distributed reguardless of the distribution of the population.

### Sampling Distribution of the Sample Mean

The sampling distribution of the sample mean will have:

- The same mean as the population mean, $\mu$
- Standard deviation [standard error] of $\frac{\sigma}{\sqrt{n}}$

It will be Normal (or approximately Normal) if either of these conditions is satisfied:

- The population distribution is Normal.
- The sample size is large (n > 30).

### Sampling Distribution of Sample Proportion

*Check the following condition before you can apply CLT. Both must be present.*
1. $np \ge 5$
1. $n(1-p) \ge 5$

If both are present then the sampling distribution of the sample proportion is...
- approximately normal
- with mean, $\mu = p$ ()
- standard deviation (standard error)
$$\sigma=\sqrt{\frac{p(1-p)}{n}}$$

### Convert Sample Proportion to Z-Score
$$z = \frac{\hat{p} - p}{\sqrt{\frac{p(1-p)}{n}}}$$