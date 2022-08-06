# countdowntimer
The countdowntimer library in Python

## Installation

#### Install from PIP

```
pip install pycountdown
```

## Formats

`countdown` can take times in these formats:

#### Seconds [+ 's']

* `10` = 10 sec
* `7.5` = 7.5 sec
* `30s` = 30 sec

#### Minutes [and seconds]

* `1m` = 1 min
* `1m 30` = 1 min, 30 sec
* `1m 23.4s` = 1 min, 23.4 sec

Note: spaces are ignored

## From a Python file

Import the library:

```python
from countdowntimer import countdown
```

Then, call the `countdown` function:

```python
countdown('1m 30')
```

The `countdown` function returns `True` if the countdown was successful, and `False` if it failed.

## From the command line

Use the `countdown` command

```
$ countdown 1m30
```

Note: if there are spaces, use quotes:

```
$ countdown "1m 30"
```
