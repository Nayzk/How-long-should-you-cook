# How-long-should-you-cook



```
# Cooking Time Calculator

This Python function calculates the adjusted cooking time for a ready-meal based on the power of the microwave being used.

## Description

The `cooking_time` function takes four parameters:
- `needed_power`: The power specified on the packaging of the ready-meal (e.g., '600W').
- `minutes`: The original cooking time in minutes.
- `seconds`: The original cooking time in seconds.
- `power`: The power of the microwave being used (e.g., '800W').

It calculates the adjusted cooking time based on the ratio of the power of the microwave being used to the needed power specified on the packaging.

## Function Implementation

```python
def cooking_time(needed_power, minutes, seconds, power):
    time = (minutes * 60 + seconds) * int(needed_power[:-1]) / int(power[:-1])
    time = int(time) + 1 if time % 1 != 0 else int(time)
    return f"{time // 60} minutes {time % 60} seconds"
```

## Example Usage

```
python
Copy code
print(cooking_time('600W', 4, 20, '800W'))  # Output: '3 minutes 15 seconds'
```

## How It Works

1. The original cooking time in seconds is calculated as `(minutes * 60 + seconds)`.
2. The power values (`needed_power` and `power`) are converted to integers by removing the last character ('W') using slicing (`[:-1]`).
3. The adjusted cooking time is calculated based on the ratio of the power of the microwave being used to the needed power specified on the packaging.
4. If the adjusted cooking time is not an integer, it is rounded up to the nearest integer.
5. The adjusted cooking time is formatted as a string in the format "X minutes Y seconds" and returned.

This function provides a convenient way to calculate the cooking time adjustment needed when using a microwave with different power settings.



## Author

- [Nayzk](https://github.com/Nayzk)