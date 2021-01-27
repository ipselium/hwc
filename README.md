# Help With Choice (HWC)

## Introduction

HWC provides the `Distribute` class. It assists the process of assigning tasks
to a population based on their choices in order of preference.

## Use

```python
from hwc import Distribute

d = Distribute(filename, pmin)   # pmin : choices to consider
d.display_optimal_possibilities()
```
