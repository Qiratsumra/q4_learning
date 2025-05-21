# 1. The Agent class has been defined as a dataclass why?
To understand how to defined an agents class as a dataclass, we need to understand 'what is a dataclass'
What is a data class?
A dataclass is a shortcut to create classes that only store data—without writing a lot of repetitive code like constructors (__init__), __repr__, and __eq__.

Without dataclass
<pre lang='markdown'>
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"
</pre>

With dataclass:
<pre lang='markdown'>
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
</pre>

## The main advantage of using @dataclass
- Less Code:
       * No need to manually write __init__, __repr__, or __eq__ methods.
- Code maintainablity and reusabilty 
       * Less code but more power


# 2a. The system prompt is contained in the Agent class as instructions? Why you can also set it as callable?
System prompt is a predefined instruction that set the behavior and rules for an assitant like how to works and behavies. Making an agents is callable, is  done by implementing the __call__() method in the class. 

# 2b. But the user prompt is passed as parameter in the run method of Runner and the method is a classmethod
In this design, the user prompt is passed as a parameter directly to the run method of the Runner class, which is defined as a classmethod. This means that instead of operating on an instance of the class, the method works with the class itself, receiving the class (cls) as its first argument. Consequently, the prompt is explicitly passed each time run is called on the class, eliminating the need for instance-level state. This approach is practical when the method's logic does not depend on individual object data but still benefits from being organized within the class namespace. Thus, you call the method directly on the class, such as Runner.run(user_prompt), making the flow straightforward and clean.

# 3. What is the purpose of the Runner class?

The purpose of a Runner class is to manage and execute a specific process or set of tasks in a controlled, organized way. Think of it as the engine or orchestrator that takes inputs, runs the core logic, and handles the flow of execution.

More specifically, a Runner class typically:
- Encapsulates the main logic of running a task, workflow, or job, making your code modular and easy to maintain.
- Abstracts the execution details so that higher-level code doesn’t have to worry about how things run internally.
- Coordinates resources and dependencies, like setting up environments, managing state, or handling exceptions.
- Often provides a clean interface to start, pause, stop, or monitor the process it controls.


## 4. What are generics in Python? Why we use it for TContext?
Generics in Python are a way to write flexible and reusable code that can work with different data types, while still maintaining type safety. Instead of hardcoding a specific type like int or str, when use a type placeholder (like T) that will be replaced with the actual type when the code is used. This is especially useful when building functions, classes, or components that should work with multiple kinds of data.

For example, imagine we have a function that gets the first item of a list. We don’t want to write separate versions of the function for lists of strings, integers, or custom objects. Instead, you define a generic type T, and let the function work with List[T]. Python’s TypeVar and Generic from the typing module allow you to define such flexible structures without losing type awareness.

Now, when it comes to TContext, this is a common pattern in web frameworks or larger applications where a “context” object is passed around. This context can hold anything — user data, database sessions, authentication tokens, or request metadata — and it might vary from one part of the application to another. Rather than locking the code into a single context structure, we use a generic TContext to keep the code open and adaptable. This allows different parts of the application to use their own context types without rewriting the logic for each one.

In simple terms, using generics like TContext makes our code smarter, more reusable, and easier to maintain. It’s like writing a function or class that works with any type of input, while still understanding what that input is supposed to be. This helps prevent bugs, improves code clarity, and keeps things scalable as your project grows.