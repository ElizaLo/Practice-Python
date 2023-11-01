# Concurrency

In Python, the things that are occurring simultaneously are called by different names **(thread, task, process)** but at a high level, they all refer to a sequence of instructions that run in order.

You might wonder why Python uses different words for the same concept. **It turns out that threads, tasks, and processes are only the same if you view them from a high level.** Once you start digging into the details, they all represent slightly different things. 

Now let’s talk about the simultaneous part of that definition. You have to be a little careful because, when you get down to the details, only multiprocessing actually runs these trains of thought at literally the same time. 

[Threading](https://realpython.com/intro-to-python-threading/) and `asyncio` both run on a single processor and therefore only run one at a time. They just cleverly find ways to take turns to speed up the overall process. Even though they don’t run different trains of thought simultaneously, we still call this concurrency.

The way the threads or tasks take turns is the big difference between `threading` and `asyncio`. In threading, the operating system actually knows about each thread and can interrupt it at any time to start running a different thread. This is called [pre-emptive multitasking](https://en.wikipedia.org/wiki/Preemption_%28computing%29#Preemptive_multitasking) since the operating system can pre-empt your thread to make the switch.

Pre-emptive multitasking is handy in that the code in the thread doesn’t need to do anything to make the switch. It can also be difficult because of that “at any time” phrase. This switch can happen in the middle of a single Python statement, even a trivial one like ``x = x +1`.

`Asyncio`, on the other hand, uses [cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking). The tasks must cooperate by announcing when they are ready to be switched out. That means that the code in the task has to change slightly to make this happen.

The benefit of doing this extra work up front is that you always know where your task will be swapped out. It will not be swapped out in the middle of a Python statement unless that statement is marked. This can simplify parts of your design.

With **multiprocessing**, Python creates new processes. A process here can be thought of as almost a completely different program, though technically they’re usually defined as a collection of resources where the resources include memory, file handles and things like that. One way to think about it is that each process runs in its own Python interpreter.

Because they are different processes, each of your trains of thought in a multiprocessing program can run on a different core. Running on a different core means that they actually can run at the same time, which is fabulous. There are some complications that arise from doing this, but Python does a pretty good job of smoothing them over most of the time.

# 📰 Articles

- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)
