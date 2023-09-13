# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*Edit your response here:*

*I think the member items give a rough idea as to what each does. As we become more familiar with the idea of computer science and the standard, more commonly practice terms/items, we realize that things like "pop" make sense. I think it is also fair to mention that different languages have different convention for the name of a method/function that does a specific operation. For example, Python a dictionary holds key value pairs as in C, a map does this.*

- To be more inline with the listed examples provided, I sort() IS a good example because it does what is says, sorts a list in place. But like all methods and functions, more research should always be done by reading the documentation as to the proper usage and implementation.
- However, I do believe there is always a bad example of this. Case in point, iter (as we know iterates) but what is not made clear is that an iter() is an object that can be iterated upon other than being iterated as is. Though, I am not fully used to the concept of the iter() or the nuances of its functionality and maybe slightly confused in my thought of this. 

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Edit your response here:*

*A dictionary differs from a list in that a dictionary is a list of unordered key/value pairs (of any type - within documented usages) separated by a colon. A list is like an array where a value of any data type can be used (Geeks for Geeks specifically says it can be homogenized). 

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Edit your response here:*

*Yes, a list does allow random access via index values. For instance, if list = [apple, orange, banana], I can access the orange with list[1], or list, index 1.*

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Edit your response here:*

- Pros:
  - It is an easy-to-use and simplistic structure, any element can be operated upon in teh same way and placed in the same data structure
  - This can be a very flexible structure where any value of any type can be mixed and matched
  - Code reuse
- Cons:
  - Overhead from operations or some form of check conversions
  - Errors from interpretation or data entry
  - One to always worry about is buggy and unexpected behaviors introduced from mixing and matching of data types, programming logic, etc.


## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Edit your responses here:*

*I would call this a mixed bag as I am familiar with some terms and methodology while others are not clear. For instance a auth() could be taken as authenticate or as author. On further inspection of the documentation outside the link above, it is used for authentication and usage permissions to a resource.*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Edit your responses here:*

*I see member functions with no more than three (at most) arguments within the requests Main Interface. However, when you move look at Request Sessions, specifically merge_environment_settings, you get many more arguments to choose from. This appears to be necessary based on the function's operations*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*Edit your responses here:*

***kwargs or key word arguments is a good thing to have because it can collect additional arguments not defined in the function's parameter list making this very flexible and updatable. The flip side is that allowing this upgradability also makes debugging harder as the expected keyword args are not necessarily known at runtime due to the nature of dynamic assignment.*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

*Edit your responses here:*

*I believe that some are set to None as a default. Simply put, because there is nothing that needs to be set. Others are set to nothing because the argument requires nothing to build. Yes argument CAN set to argument to be a predetermined value and it IS a good idea in some cases. For instance, you do not want a bug crashing value or lack there of - a division by zero instance comes to mind or perhaps something like having negative value when a known positive value is the only correct value that can be set.*
