# S2: Quartiles and spread

## Quartiles and percentiles
(Q1, Q2, Q3 in one sentence each. Why do tools disagree?)

## Five-number summary and box plot
(What each part of a box plot shows. The 1.5 x IQR rule.)

## Measures of spread
| Measure | Formula | Units | Robust? | Use when |
|---|---|---|---|---|
| Range | | | | |
| IQR | | | | |
| Variance | | | | |
| Standard deviation | | | | |
| CV | | | | |

## Population vs sample formulas
(Why n - 1? Which library uses which default?)

| Tool | var/std default |
|---|---|
| numpy | |
| pandas | |
| statistics | |

## z-scores
(Formula, meaning, the masking problem)

## Empirical rule vs Chebyshev

## Mistakes I made / predictions I got wrong

## Questions I still have

What are quartiles, and what is the IQR? Why is the IQR robust?
How does a box plot show an outlier? What is the 1.5 × IQR rule?
Why do numpy and statistics give different quartiles for the same data?
What is the difference between variance and standard deviation? Why prefer the SD for reporting?
Why does the sample variance divide by n − 1?
What is the default ddof in NumPy, and in pandas?
What is a z-score, and what does a z-score of −2 mean?
What is the 68-95-99.7 rule, and when does it apply? What does Chebyshev add?
When would you use the coefficient of variation?
Why can an outlier hide from a z-score rule?
What happens to the mean and standard deviation if you add a constant to every value? Multiply by a constant?
Two datasets have the same mean. How do you compare them?