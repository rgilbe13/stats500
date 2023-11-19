## Comparing Two Independent Proportions
Categorical - Taken from two distince groups

*Minitab: Stat->Basic Statistics->2 Proportions*

- Explainatory Variable: Categorical
- Response Variable: Categorical

### Check Conditions (all are > 5)

$$n_1\hat{p}_1,n_1(1-\hat{p}_1),n_2\hat{p}_2,n_2(1-\hat{p}_2)$$

### Confidence Interval

$$\hat{p}_1-\hat{p}_2\pm z_{\alpha/2}\sqrt{\dfrac{\hat{p}_1(1-\hat{p}_1)}{n_1}+\dfrac{\hat{p}_2(1-\hat{p}_2)}{n_2}}$$

### Hypothesis Testing
$H_0\colon p_1-p_2=0$

$H_0\colon p_1-p_2\ne0$

$$\hat{p}^*=\dfrac{x_1+x_2}{n_1+n_2}$$

$$z^*=\dfrac{(\hat{p}_1-\hat{p}_2)-0}{\sqrt{\hat{p}^*(1-\hat{p}^*)\left(\dfrac{1}{n_1}+\dfrac{1}{n_2}\right)}}$$

## Comparing Two Independent Means
Quantitative - taken from two distince groups
- Explainatory Variable: Categorical
- Response Variable: Quantitative

*Minitab: Stat->Basic Statistics->2-Sample t*
- check assume equal variance for pooled
- UnCheck assume equal variance for un-pooled

### *Determine pooled vs unpooled variances*

Use pooled variance if the standard eviation ratio falls between 0.5 and 2
$$.5 < \frac{s_1}{s_2} < 2$$

## Using Pooled Variances
### Common Standard Deviation

$$s_p=\sqrt{\dfrac{(n_1-1)s_1^2+(n_2-1)s^2_2}{n_1+n_2-2}}$$

### Confidence Interval

$$\bar{x}_1-\bar{x}_2\pm t_{\alpha/2}s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}$$

where $t_{\alpha/2}$ comes from a t-distribution with $n_1+n_2-2$ degrees of freedom.

### Hypothesis Testing

$$H_0\colon\mu_1-\mu_2=0, H_a\colon \mu_1-\mu_2\ne0$$

The assumptions/conditions are:

- The populations are independent
- The population variances are equal
- Each population is either normal or the sample size is large (n > 30).

*If assumptions are not met. Use Minitab **Normal Probability Plot***

$$t^*=\dfrac{\bar{x}_1-\bar{x}_2-0}{s_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}$$

## Un-Pooled Variance

**Degrees of freedom calculation can be made by choosing the smaller of $n_1-1$ and $n_2-1$.**

### Checkk Conditions

- The populations are independent
- Each population is either normal or the sample size is large.

### Confidence Interval

$$\bar{x}_1-\bar{x}_2\pm t_{\alpha/2} \sqrt{\frac{s^2_1}{n_1}+\frac{s^2_2}{n_2}}$$

## Hypothesis Testing


$$t^*=\dfrac{\bar{x}_1-\bar{x_2}-0}{\sqrt{\frac{s^2_1}{n_1}+\frac{s^2_2}{n_2}}}$$


## Comparing Two Dependent Means
Quantitative - taken from each subject (paired)
- Explainatory Variable: None
- Response Varibale: Quantative

*Minitab: Stat->Basic Paired t*


### Check Conditions
- Each population is either normal or the sample size is large.

### Confidence Interval

$$\bar{d}\pm t_{\alpha/2}\frac{s_d}{\sqrt{n}}$$

### Hypothesis Testing
$H_0\colon \mu_d=0$

$H_a\colon \mu_d\ne 0$

$$t^*=\dfrac{\bar{d}-0}{\frac{s_d}{\sqrt{n}}}$$

t-distribution with $n-1$ degrees of freedom.

## F-Test to Compare Two Population Variances
*Minitab: Stat->Basic Statistics->2-Variances*
$H_0\colon \dfrac{\sigma^2_1}{\sigma^2_2}=1$

$H_a\colon \dfrac{\sigma^2_1}{\sigma^2_2}\ne1$