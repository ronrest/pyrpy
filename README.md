# Introduction
pyRpy is a Python package that allows you to perform statistical analysis in 
Python using the arguably more intuitive R style function names. It is intended 
for those that fall into one or more of the following categories:

1. Someone that uses python and R interchangeably in their workflow and wishes 
to minimise the number of function names (and function arguments) to memorise.
2. Someone who wants to quickly and easily port their R scripts into python. 
3. Someone who wishes to migrate their statistical workflow from R into Python, 
with the least steep learning barrier. 
4. Someone that enjoys the ease and power with which you can create general 
purpose programs in Python, but which prefers the ease with which you can 
perform statistical analysis in R. 


If you fall into one or more of the above categories, then this module is 
perfect for you. It allows you to do statistical analysis using pretty much the 
exact same function calls you would use in R (with a few minor 
exceptions/adjustments).This allows you to leverage the full potential that a 
general purpose programming language like Python has to offer, with the benefits 
of using the intuitive R function calls.

Currently there are some great libraries in python for performing statistical
analysis (numpy, scipy, pandas), but they are spread out across many libraries
and they often times make use of cumbersome unintuitive naming conventions
for the functions.

pyRpy aims to make use of these great statistical packages in python, but hide
their cumbersome nature. It aims to use naming conventions that are on most
occasions exactly the same as the functions in R.

This makes it great if you are transitioning between R, and starting out in
python. Your learning curve will not be as steep. You will be able to copy and
paste large chunks of your existing R code, and make only some minor
modifications.

# Installing
This project is very much in the early stages of development, and potentially 
unstable, but if you wish to try it out, then run the following in a command line. 

```
pip install -e git+https://github.com/ronrest/pyrpy.git#egg=pyrpy
```

You may need to use `sudo` at the start if you are instlaling from a debian based linux distribution. 



# Development Notes
This is a very new project, and only has one person working on it at the moment
based on functions that are most used by the developer. Please see the "Help Us"
subsection for ways in which you can contribute to the project.

Here is a list of functions that have been implemented so far:

    c() **
    mean()
    sd()
    sort() * 
    
    factorial()
    choose()
    nck() +  
    npk() +
    
    rbinom()
    dbinom()
    qbinom()
    pbinom()
    cbinom() + 
    
    rnorm()
    dnorm()
    qnorm()
    pnorm()
    cnorm() +
    
    plot_distribution() * +
    
\* Refers to functions that have only been partially implemented. There may be 
arguments missing (See the docstrings for those functions to see what has and 
has not been implemented).

** Refers to functions that do not quite behave 100% the way you would expect 
the equivalent function in R to behave (See the docstrings for those functions 
to see what behaviour is different).

\+ refers to functions that are not core functions of R, but which have been 
introduced as part of my R convenience packages ( https://github.com/ronrest/convenience_functions_R ).

# Help Us!
You can contribute by:
- Cloning this repository, writing new code and merging with the master branch.
- Creating code snippets, and sending them to us, and we will add them to the
repository.
- Telling us about a function that we have not yet implemented from R, along
with providing us with an analogous function (or set of functions) in python
(preferably using just the core libraries, plus numpy,scipy or pandas), and how
the arguments that are used in R map the the arguments that are used in the
python functions.
- Testing the functions under a wide range of circumstances to see if the 
outputs indeed match what you would get using R. 


