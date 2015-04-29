---
output:
  html_document:
    number_sections: yes
    toc: yes
---
# Introduction
**Do you enjoy the ease and power with which you can create general purpose
programs in python?**

- yes

**But do you prefer the ease with which you can perform statistical analyses in R?**

- yes

**Do you believe that this ease with which you can perform statistical analyses in
R is due to the simple and intuitive naming conventions of functions in R?**

- yes

If you answered yes to the above questions, then this module is perfect for you.
It allows you to do statistical analysis using pretty much the exact same
function calls you would use in R (with a few minor exceptions/adjustments).
This allows you to leverage the full potential that a general purpose programming
language like python has to offer, with the benefits of using the intuitive R
function calls.

Currently there are some great libraries in python for performing statistical
analysis (numpy, scipy, pandas), but they are spread out across many libraries
and they often times make use of cumbersome unintuitive naming conventions
for the functions.

pyRpy aims to make use of these great statistical packages in python, but hide
their cumbersome nature. It aims to use naming conventions that are on most
occasions direct analogues of of the same kind of functions in R.

This makes it great if you are transitioning between R, and starting out in
python. Your learning curve will not be as steep. You will be able to copy and
paste large chunks of your existing R code, and make only some minor
modifications.


# Development Notes
This is a very new project, and only has one person working on it at the moment
based on functions that are most used by the developer. Please see the "Help Us"
subsection for ways in which you can contribute to the project.

Here is a list of functions that have been implemented so far:

    rbinom()
    dbinom()
    qbinom()
    pbinom()

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

