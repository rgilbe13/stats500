import math

hyp="H_0: p_1-p_2=0, H_1:p_1-p_2\\ne0"

p1=1674
n1=4881
p2=1808
n2=5181

ph1=p1/n1
ph2=p2/n2
pstar=(p1+p2)/(n1+n2)
zstar=(ph1-ph2)/math.sqrt(pstar*(1-pstar)*((1/n1)+(1/n2)))

n1_spec="n_1=" + str(n1) + ", \\hat p_1=\\frac{" + str(p1) + "}{" + str(n1) + "}=" + str(ph1)
n2_spec="n_2=" + str(n2) + ", \\hat p_2=\\frac{" + str(p2) + "}{" + str(n2) + "}=" + str(ph2)
phat_spec="\\hat{p}^*=\\frac{x_1+x_2}{n_1+n_2}=\\frac{%d+%d}{%d+%d}=\\frac{%d}{%d}=%.3f"
z_spec="z^*=\\frac{\\hat{p}_1-\\hat{p}_2-0}{\\sqrt{\\hat{p}^*(1-\\hat{p}^*)\\left(\\frac{1}{n_1}+\\frac{1}{n_2}\\right)}}=\\frac{\\frac{%d}{%d}-\\frac{%d}{%d}}{\\sqrt{%.3f(1-%.3f)\\left(\\frac{1}{%d}+\\frac{1}{%d}\\right)}}=%.3f"

print("ph1: " + str(ph1))
print("ph2: " + str(ph2))
print("pstar: " + str(pstar))
print("zstar: " + str(zstar))
print("Hypothesis:")
print(hyp)
print("Test Statistic:")
print(n1_spec)
print(n2_spec)
print(phat_spec % (p1, p2, n1, n2, (p1+p2), (n1+n2), (p1+p2)/(n1+n2)))
print(z_spec % (p1, n1, p2, n2, pstar, pstar, n1, n2, zstar))