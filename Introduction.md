# what is python ?
  * Python is a high-level general purpose programming language:
    * Because code is automatically compiled to byte code and executed, Python is suitable for use as a scripting language, Web application implementation language, etc.
    * Because Python can be extended in C and C++, Python can provide the speed needed for even compute intensive tasks.
    * Because of its strong structuring constructs (nested code blocks, functions, classes, modules, and packages) and its consistent use of objects and object-oriented programming, Python enables us to write clear, logical applications for small and large tasks.
  * Important features of Python:
    * Built-in high level data types: strings, lists, dictionaries, etc.
    * The usual control structures: if, if-else, if-elif-else, while, plus a powerful collection iterator (for).
    * Multiple levels of organizational structure: functions, classes, modules, and packages. These assist in organizing code. An excellent and large example is the Python standard library.
    * Compile on the fly to byte code -- Source code is compiled to byte code without a separate compile step. Source code modules can also be "pre-compiled" to byte code files.
    * Object-oriented -- Python provides a consistent way to use objects: everything is an object. And, in Python it is easy to implement new object types (called classes in object-oriented programming).
  * Some things you will need to know:

    Python uses indentation to show block structure. Indent one level to show the beginning of a block. Out-dent one level to show the end of a block. As an example, the following C-style code:
```
    if (x)
    {
        if (y)
        {
            f1()
        }
        f2()
    }
```
    in Python would be:
```
    if x:
        if y:
            f1()
        f2()
```
And, the convention is to use four spaces (and no hard tabs) for each level of indentation. Actually, it's more than a convention; it's practically a requirement. Following that "convention" will make it so much easier to merge your Python code with code from other sources.

## An overview of Python:

   * A scripting language -- Python is suitable (1) for embedding, (2) for writing small unstructured scripts, (3) for "quick and dirty" programs.

   * Not a scripting language -- (1) Python scales. (2) Python encourages us to write code that is clear and well-structured.

   * Interpreted, but also compiled to byte-code. Modules are automatically compiled (to .pyc) when imported, but may also be explicitly compiled.

   * Provides an interactive command line and interpreter shell. In fact, there are several.

   * Dynamic -- For example:
        * Types are bound to values, not to variables.
        * Function and method lookup is done at runtime.
        * Values are inspect-able.
        * There is an interactive interpreter, more than one, in fact.
        * You can list the methods supported by any given object.

   * Strongly typed at run-time, not compile-time. Objects (values) have a type, but variables do not.

   * Reasonably high level -- High level built-in data types; high level control structures (for walking lists and iterators, for example).

   * Object-oriented -- Almost everything is an object. Simple object definition. Data hiding by agreement. Multiple inheritance. Interfaces by convention. Polymorphism.

   * Highly structured -- Statements, functions, classes, modules, and packages enable us to write large, well-structured applications. Why structure? Readability, locate-ability, modifiability.

   * Explicitness

   * First-class objects:
        Definition: Can (1) pass to function; (2) return from function; (3) stuff into a data structure.
        Operators can be applied to values (not variables). Example: f(x)[3]

   * Indented block structure -- "Python is pseudo-code that runs."

   * Automatic garbage collection. (But, there is a gc module to allow explicit control of garbage collection.)
