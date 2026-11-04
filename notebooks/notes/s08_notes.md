# S8: NumPy

## List vs array
| | list | ndarray |
|---|---|---|
| Types | | |
| Memory | | |
| + and * | | |
| Speed, and why | | |

## dtypes
(Common dtypes, upcasting, overflow, astype)

## Vectors
(Element-wise ops, dot product, norm, cosine similarity, aggregations)

## Matrices
| Operation | Syntax | Shape rule |
|---|---|---|
| element-wise | | |
| matrix product | | |
| transpose, inverse, solve | | |

## Indexing and slicing
(1-D, 2-D, negative, step, fancy, boolean. View vs copy table.)

## Broadcasting
(The rule. Three examples. The keepdims trap.)

## axis
(What axis=0 and axis=1 mean on a 2-D array)

## Vectorisation
(Why loops are replaced. One example with times.)



What is the difference between a Python list and a NumPy array?
Why are NumPy operations so much faster than Python loops?
What is a dtype? What happens if you add 10 to a uint8 array holding 250?
What is the difference between *, @, and np.dot?
What is broadcasting? State the rule, and give an example that fails.
What does axis=0 mean when you call a.sum(axis=0) on a 2-D array?
What is the difference between a view and a copy? Which operations return which?
How do you select rows with a condition? Why do you need & and parentheses, not and?
What is the difference between reshape, ravel, and flatten?
What are the default ddof values for np.std, np.var, and np.cov, and what are pandas’ defaults?
How do you deal with missing values in NumPy?
What does np.where do? Give two uses.