# Step 4: Dependency Injection

In this step, you'll learn about Dependency Injection in FastAPI. Dependency Injection is a way to share reusable code (like checking user permissions or connecting to a database) across your API endpoints. FastAPI makes it easy to create and use dependencies, keeping your code clean and organized.

### Why Use Dependency Injection?
* Code Reusability: Define common logic or resources once and reuse them across multiple endpoints (e.g., fetching the current user).
* Separation of Concerns: Keep your endpoint logic focused on the specific task, delegating common tasks (like authentication or fetching shared data) to dependencies.
* Testability: Easily replace dependencies with mock objects during testing.
* Organization: Structure your application logic cleanly.

### How It Works
- Define a Dependency: Create a function (or a class with __call__) that performs the necessary setup or provides the required resource. This function can itself have parameters (which FastAPI will also resolve, potentially including other dependencies).
- "Depend" on It: Add a parameter to your path operation function, type-hinted with the return type of the dependency function, and use Depends(your_dependency_function) as the default value. Use typing.Annotated for cleaner syntax.

FastAPI will execute the dependency function for each request that requires it and pass the result to your endpoint function. FastAPI also caches the result within the same request, so if multiple parts of your request handling depend on the same dependency function, it's only executed once per request.