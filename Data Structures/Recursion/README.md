# Recursion in Python

**In Python**, each time a function (recursive or otherwise) is called, a struc- ture known as an **_activation record_** or **_frame_** is created to store information about the progress of that invocation of the function.

When the execution of a function leads to a nested function call, the execution of the former call is suspended and its **activation record stores the place in the source code** at which the flow of control should continue upon return of the nested call.
