# Math_Series

[Link to Latest PR](https://github.com/ticochuck/math_series/pull/1)

## Description
- The fibonacci function has one parameter n. The function returns the nth value in the fibonacci series. 

- The lucas function returns the nth value in the lucas numbers. 

Both the fibonacci series and the lucas numbers are based on an identical formula. The function sum_series has one required parameter and two optional parameters. The required parameter determines which element in the series to print. The two optional parameters have default values of 0 and 1 and determine the first two values for the series to be produced.

Calling the sum_series function with no optional parameters produce numbers from the fibonacci series. Calling it with the optional arguments produce values from the lucas numbers. 

## Usage

The function sum_series can be called in 2 different ways. 
To use this application, call the function sum_series with at least 1 parameter. This parameter will determine the nth number to return from the fibonacci or lucas series. If you call the sum_series function with 3 parameters, the first parameter will determine the nth number to return from the lucas series, and the next 2 parameter will be the first 2 number in the lucas series. The function only accepts parameters that are integers greater than 0. It it is called with a parameter that does not meet the requeriements, it will print an error message.

```
sum_series(6)
    returns Fibonacci of 6 is 8

sum_series(6, 1, 3)
    returns Lucas of 8 with 1 and 3 is 76

sum_series(6.3) or sum_series('one')
    return Parameter(s) must be intergers >= 0
```

## Challenges

- Earlier in the week I had issues installing poetry, but thanks to Roger I got poetry up and running before I had to work on this lab 

- It was confusing having to create the virtual enviorment for the first time

- Writing tests is interesting. I am not sure if I am missing any key points, but at least for this lab, it was not too hard 


## References

[Fibonacci](https://www.youtube.com/watch?v=Qk0zUZW-U_M)
After I had already completed my code, I watched this video and it looks like is is a better way to get the nth value. However, I wanted to keep it the way I had it originally because I can pass high values without needing to import lru_cache to be efficient. 

## Lab02 - Modules, Containers, and Testing

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160025)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)
