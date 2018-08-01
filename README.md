# Python Scientific 
The repository contains some of the must have scientific library functions which are not defined in scipy and numpy for general purpose use.

### Usage
```python
import numpy as np
import fspecial

np.set_printoptions(precision=4)

print(fspecial.fspecial('gaussian'))
```
```
[[0.0113 0.0838 0.0113]
 [0.0838 0.6193 0.0838]
 [0.0113 0.0838 0.0113]]
```

```python
print(fspecial.fspecial('gaussian',4,3))
```

```
[[0.0558 0.0623 0.0623 0.0558]
 [0.0623 0.0696 0.0696 0.0623]
 [0.0623 0.0696 0.0696 0.0623]
 [0.0558 0.0623 0.0623 0.0558]]
```

```python
print(fspecial.fspecial('average',6))
```

```python
[[0.25 0.25]
 [0.25 0.25]]
```