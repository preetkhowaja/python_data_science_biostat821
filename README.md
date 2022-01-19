# Python Functions for Data science

This repository contains code that has two main functions in the file **functions.py** as follows:

### `get_data()`
_accepts_: a file path (string) and

_outputs_: a list of lists of integers.

The file will contain two lines of integers separated by spaces, for example:

```text
1 44 31 4 5 6
21 3 2 13 55 72
```

### `analyze_data()`
_accepts_:
1. a list of lists of integers and
2. a string option that can be one of the following:
    * `"average"` (of all the data together)
    * `"standard deviation"` (of all the data together)
    * `"covariance"` (between the two lists)
    * `"correlation"` ([Pearson's correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient))
and

_outputs_: a floating-point number.
