# Probability

## Notation

|Term|Definition|
|---|---|
|Event|A collection of outcomes, typically denoted by capital letters such as A, B, C, etc...|
|Outcome Space|The outcome space of a scenario is all the possible outcomes that can occur and is often denoted S. The outcome space may also be referred to as the sample space|
|Union|The union of two events, A and B, contains all of the outcomes that are in A, B or both. In statistics, ‘or’ means at least one event occurs and therefore includes the event where both occur.|
Interesction|The intersection of two events, A and B, contains all of the outcomes that are in both A and B.|
|Mutually Exclusive|A and B are called mutually exclusive (or disjoint) if the occurrence of outcomes in A excludes the occurrence of outcomes in B.  One example of two mutually exclusive events is A and A'.|
|Complement|The complement of an event, A, contains all of the outcomes that are not in A.|
|Conditional Probability|The probability of one event occurring given that it is known that a second event has occurred.|
|Marginal Probability|The probability of an event without reference to any other event or events occurring.|
|Independent Events|Two events, A and B, are considered independent events if the probability of A occurring is not changed based on any knowledge of the outcome of B.|
|Dependent Events|Two events are not independent, or dependent if the knowledge of the outcome of B changes the probability of A. |
|Prevalence|is the probability or proportion of occurrence of a disease or behavior in the population at a particular point in time.|
|Sensitivity|is the probability of a positive result given person is actually positive.|
|Specificity|is the probability of a negative result given person is actually negative. |
|False Positive|are when results come back positive for someone who is actually negative |
|False Negative|are when results come back negative for someone who is actually positive |


### Converting to Probability Notation

1. Identifying the outcome event of interest: {Getting a Tail when we toss a fair coin}.
1. Use a single letter or word to represent this outcome of interest: T={Getting a Tail when we toss a fair coin}, for instance.
1. State your interest in the probability of this outcome: P(T) which is read, "Probability of getting a Tail when we toss a fair coin."


### Set Notation

Write all the possible outcomes of rolling 2 dice in set notation.

S = {(1,1) (2,1) (3,1) (4,1) (5,1) (6,1) (1,2) (2,2) (3,2) (4,2) (5,2) (6,2) (1,3) (2,3) (3,3) (4,3) (5,3) (6,3) (1,4) (2,4) (3,4) (4,4) (5,4) (6,4) (1,5) (2,5) (3,5) (4,5) (5,5) (6,5) (1,6) (2,6) (3,6) (4,6) (5,6) (6,6)}

There are 36 possible outcomes in the sample space S.

*Example*

Let B = {sum of the two faces is greater than or equal to 10}

In set notation...

B = {(6, 4), (5, 5), (6, 5), (4, 6), (5, 6), (6,6)}

## Set Operations

### Union
The union of two events, A and B, contains all of the outcomes that are in A, B or both. In statistics, ‘or’ means at least one event occurs and therefore includes the event where both occur.

Represented as $ A \cup B$

### Intersection
The intersection of two events, A and B, contains all of the outcomes that are in both A and B.

Represented as $A \cap B$

### Complement
The complement of an event, A, contains all of the outcomes that are not in A.
 Represented as $A\complement=\bar{A}=A'$
### Mutually Exclusive
A and B are called mutually exclusive (or disjoint) if the occurrence of outcomes in A excludes the occurrence of outcomes in B.  One example of two mutually exclusive events is A and A'.

There are no elements in $A \cap B$ and thus $A \cap B = \emptyset$ . The empty set, denoted as $\emptyset$ , is an event that contains no outcomes.

## Interruptations of Probability

1. **Classical Interpretation of Probability**

    The probability that event E occurs is denoted by P(E). When all outcomes are equally likely.

    $P(E) = \frac{\text{number of outcomes in E}}{\text{number of possible outcomes}}$

1. **Subjective Probability**

    Subjective probability reflects personal belief which involves personal judgment, information, intuition, etc.

    For example, what is P (you will get an A in a certain course)? Each student may have a different answer to the question.

1. **Relative Frequency Concept of Probability (Empirical Approach)**

    If a particular outcome happens over a large number of events then the percentage of that outcome is close to the true probability.

    For example, if we flip the given coin 10,000 times and observe 4555 heads and 5445 tails, then for that coin, P(H)=0.4555.    

    $P(E) \approx \frac{\text{number of outcomes in E}}{\text{number of possible outcomes}}$

## Probability Properties

**Probability of an event**

Probabilities will always be between (and including) 0 and 1. A probability of 0 means that the event is impossible. A probability of 1 means an event is guaranteed to happen. A probability close to 0 means the event is "not likely" and a probability close to 1 means the event is "highly likely" to occur. We denote the probability of event A as P(A).

$0 \le P(A) \le 1$

**Probability of a complement**

If A is an event, then the probability of A is equal to 1 minus the probability of the complement of $A\complement$.

$P(A) = 1 - P(A\complement)$

We can see from the formula that $1 = P(A) + P(A\complement)$

**Probability of the empty set**

If A and B are mutually exclusive, then $A \cap B = \emptyset$. Therefore, $P(A \cap B) = 0$. This is important when we consider mutually exclusive (or disjoint) events.

$P(A \cap B) = 0$

**Probability of the union of two events**

$P(A \cup B) - P(A) + P(B) - P(A \cap B)$

If A and B are mutually exclusive, then $P(A \cup B) = P(A) + P(B)$.


## Conditional Probability
The probability of A given B:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
The probability of B given A
$$P(B|A) = \frac{P(B \cap A)}{P(A)}$$

### The Probability of the Intersection of Dependent Events
The probability of dependent events A and B derived from the formulas for conditional probability:

$$P(A \cap B) = P(B)P(A|B)$$

$$P(B \cap A) = P(A)P(B|A)$$

Note:
$$P(A|B) \ne P(B|A)$$

$$P(A|B) = 1 - P(A\complement|B)$$

$$P(A)=P(A \cap B) + P(A \cap B\complement)=P(A|B)P(B) + P(A|B\complement)P(B\complement)$$


## Independent Events
We can see that in some situations, the conditional and marginal probabilities are different and for some situations, the two probabilities may be equal. When they are equal, the events are independent events, when they are not equal, they are not independent events.

Unless one is explicitly told that events are independent, one cannot simply assume that they are. We can check for independence of two events by showing that any ONE of the following is true. For any given probabilities for events A and B, the events are independent if:
### Not a formula (Conditional Checks)
$$P(A \cap B) = P(A) \times P(B)$$

$$P(A|B)=P(A)$$

$$P(B|A)=P(B)$$

## Bayes Theorem
The use of Bayes' theorem to find "reverse" conditional probabilities.

$$P(A_{i}|B)=\dfrac{P(B | A_{i})P(A_{i})}{\sum_{i} P(B | A_{i})P(A_{i})}=\dfrac{P(B | A_{i})P(A_{i})}{P(B| A_{1})P(A_{1})+P(B |A_{2})P(A_{2})+...+P(B| A_{k})P(A_{k})}$$

Apply to only 2 events...

$$P(A_{i}|B)=\dfrac{P(B | A_{i})P(A_{i})}{\sum_{i} P(B | A_{i})P(A_{i})}=\dfrac{P(B | A_{i})P(A_{i})}{P(B| A_{1})P(A_{1})+P(B |A_{2})P(A_{2})+...+P(B| A_{k})P(A_{k})}$$

### Helpful formulas
$$P(A)=P(A \cap B) + P(A \cap B\complement)$$

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

$$P(A \cap B) = P(B)P(A|B)$$

Testing cut off...