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

# ❓ When Is Concurrency Useful?

Concurrency can make a big difference for two types of problems. These are generally called **CPU-bound** and **I/O-bound**.

I/O-bound problems cause your program to slow down because it frequently must wait for [input/output (I/O)](https://realpython.com/python-input-output/) from some external resource. They arise frequently when your program is working with things that are much slower than your CPU.

<img src="" width="700" height="394"/>

In the diagram above, the blue boxes show time when your program is doing work, and the red boxes are time spent waiting for an I/O operation to complete. This diagram is not to scale because requests on the internet can take several orders of magnitude longer than CPU instructions, so your program can end up spending most of its time waiting.

On the flip side, there are classes of programs that do significant computation without talking to the network or accessing a file. These are the CPU-bound programs, because the resource limiting the speed of your program is the CPU, not the network or the file system.

Here’s a corresponding diagram for a CPU-bound program:

<img src="" width="700" height="394"/>

As you work through the examples in the following section, you’ll see that different forms of concurrency work better or worse with CPU-bound and I/O-bound programs. Adding concurrency to your program adds extra code and complications, so you’ll need to decide if the potential speed up is worth the extra effort.

# 💠 Threads

It’s tempting to think of threading as having two (or more) different processors running on your program, each one doing an independent task at the same time. That’s almost right. The threads may be running on different processors, but they will only be running one at a time.

Getting multiple tasks running simultaneously requires a non-standard implementation of Python, writing some of your code in a different language, or using `multiprocessing` which comes with some extra overhead.

Because of the way CPython implementation of Python works, threading may not speed up all tasks. This is due to interactions with the GIL that essentially limit one Python thread to run at a time.

## Daemon Threads

In computer science, a [daemon](https://en.wikipedia.org/wiki/Daemon_(computing)) is a process that runs in the background.

Python threading has a more specific meaning for daemon. A daemon thread will shut down immediately when the program exits. One way to think about these definitions is to consider the daemon thread a thread that runs in the background without worrying about shutting it down.

If a program is running Threads that are not daemons, then the program will wait for those threads to complete before it terminates. Threads that are daemons, however, are just killed wherever they are when the program is exiting.

## ℹ️ Notes

The other interesting change in our example is that each thread needs to create its own `requests.Session()` object. When you’re looking at the documentation for requests, it’s not necessarily easy to tell, but reading [this issue](https://github.com/requests/requests/issues/2766), it seems fairly clear that you need a separate Session for each thread.

This is one of the interesting and difficult issues with threading. Because the operating system is in control of when your task gets interrupted and another task starts, any data that is shared between the threads needs to be protected, or thread-safe. Unfortunately requests.Session() is not thread-safe.

There are several strategies for making data accesses thread-safe depending on what the data is and how you’re using it. One of them is to use thread-safe data structures like Queue from Python’s queue module.

Well, as you can see from the example, it takes a little more code to make this happen, and you really have to give some thought to what data is shared between threads.

---

The correct number of threads is not a constant from one task to another. Some experimentation is required.

## 📰 Articles

- [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
  - :octocat: [intro-to-threading](https://github.com/realpython/materials/tree/master/intro-to-threading)
- [`threading` Version](https://realpython.com/python-concurrency/#threading-version)
- [Daemon (computing)](https://en.wikipedia.org/wiki/Daemon_(computing)) on Wikipedia

## ⚙️ Tools

- [`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html#module-threading)

# 💠 asyncio 

## ℹ️ Notes

An important point of `asyncio` is that the tasks never give up control without intentionally doing so. They never get interrupted in the middle of an operation. This allows us to share resources a bit more easily in `asyncio` than in threading. You don’t have to worry about making your code thread-safe.

## 📰 Articles

- [`asyncio` Version](https://realpython.com/python-concurrency/#asyncio-version)
- [How does asyncio work?](https://stackoverflow.com/a/51116910/6843734)

# 📰 Articles

- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)
- - [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
 
# 🗞️ Other Related Topics and Articles

## ◾ Wikipedia

- [Daemon (computing)](https://en.wikipedia.org/wiki/Daemon_(computing))
- [Race condition](https://en.wikipedia.org/wiki/Race_condition)
- [Preemption (computing)](https://en.wikipedia.org/wiki/Preemption_%28computing%29#Preemptive_multitasking)
- [Cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking)
- [Mutual exclusion](https://en.wikipedia.org/wiki/Mutual_exclusion)
