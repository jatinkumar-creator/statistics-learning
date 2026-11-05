# S9: pandas I

## pandas vs NumPy
(Labels, per-column dtypes, alignment, missing values)

## Series
(What it holds; creating one; alignment; idxmax vs argmax)

## DataFrame
(Index, columns, dtypes; df["a"] vs df[["a"]]; set_index; why avoid df.a)

## Loading data
| Source | Function | Key parameters | Common problem |
|---|---|---|---|
| CSV | | | |
| Excel | | | |
| HTML | | | |

## Accessing data
| Accessor | By | Slice end | Use for |
|---|---|---|---|
| loc | | | |
| iloc | | | |
| at | | | |
| iat | | | |
| head / tail / sample | | | |

## Traps
(Chained assignment; labels vs positions after filtering; the to_csv index)

## Mistakes I made / predictions I got wrong

## Questions I still have




What are a Series and a DataFrame? How do they relate to NumPy arrays?
How do pandas and NumPy differ when you add two objects?
What is the difference between loc and iloc? Which slice includes its end?
What is the difference between at and loc, and between iat and iloc? When do you use at?
What does df["a"] return, and what does df[["a"]] return?
How do you read a CSV with thousands separators, dates, and missing codes like "N/A"?
How do you read all the sheets of an Excel workbook? What does read_html return?
Why does read_csv sometimes turn an integer column into floats?
What is the index for? What do set_index and reset_index do?
What is chained assignment, and why is it a bug?
How would you read a 10 GB CSV that doesn’t fit in memory?
Why should you pass index=False to to_csv?