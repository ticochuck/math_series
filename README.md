# Math_Series

By [Chuck Li Villalobos](https://github.com/ticochuck)


## Description
- The fibonacci function has one parameter n. The function returns the nth value in the fibonacci series. 

- The lucas function returns the nth value in the lucas numbers. 

Both the fibonacci series and the lucas numbers are based on an identical formula. The function sum_series has one required parameter and two optional parameters. The required parameter determines which element in the series to print. The two optional parameters have default values of 0 and 1 and determine the first two values for the series to be produced.

Calling this function with no optional parameters produce numbers from the fibonacci series. Calling it with the optional arguments produce values from the lucas numbers. 

## Usage

The function sum_series can be called in 2 different ways. 
To use this application, call the function sum_series with at least 1 parameter. This parameter will determine the nth number to return from the fibonacci or lucas series. If you call the sum_series function with 3 parameters, the first parameter will determine the nth number to return from the lucas series, and the next 2 parameter will be the first 2 number in the lucas series. 

```
sum_series(6)
returns Fibonacci of 6 is 8
sum_series()
returns Lucas of 8 with 1 and 3 is 76
```

### Known Issues

If you discover any bugs, feel free to create an issue on GitHub fork and
send us a pull request.

[Issues List](Github Issues List URL goes here).


### References

[Fibonacci](https://www.youtube.com/watch?v=Qk0zUZW-U_M)
After I had already completed my code, I watched this video and it looks like is is a better way to get the nth value. However, I wanted to keep it the way I had it originally because I can pass high values without needing to import lru_cache to be efficient. 


## Authors

* Chuck Li Villalobos
