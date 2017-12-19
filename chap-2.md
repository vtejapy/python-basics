# Lexical matters
## Lines

   * Python does what you want it to do most of the time so that you only have to add extra characters some of the time.
   * Statement separator is a semi-colon, but is only needed when there is more than one statement on a line. And, writing more than one statement on the same line is considered bad form.
   * Continuation lines -- A back-slash as last character of the line makes the following line a continuation of the current line. But, note that an opening "context" (parenthesis, square bracket, or curly bracket) makes the back-slash unnecessary.

## Comments

   * Everything after "#" on a line is ignored. No block comments, but doc strings are a comment in quotes at the beginning of a module, class, method or function. Also, editors with support for Python often provide the ability to comment out selected blocks of code, usually with "##".
## Names and tokens

   * Allowed characters: a-z A-Z 0-9 underscore, and must begin with a letter or underscore.
   * Names and identifiers are case sensitive.
   * Identifiers can be of unlimited length.
   * Special names, customizing, etc. -- Usually begin and end in double underscores.
   * Special name classes -- Single and double underscores.
        * Single leading single underscore -- Suggests a "private" method or variable name. Not imported by "from module import *".
        * Single trailing underscore -- Use it to avoid conflicts with Python keywords.
        * Double leading underscores -- Used in a class definition to cause name mangling (weak hiding). But, not often used.
   * Naming conventions -- Not rigid, but:
        * Modules and packages -- all lower case.
        * Globals and constants -- Upper case.
        * Classes -- Bumpy caps with initial upper.
        * Methods and functions -- All lower case with words separated by underscores.
        * Local variables -- Lower case (with underscore between words) or bumpy caps with initial lower or your choice.
        * Good advice -- Follow the conventions used in the code on which you are working.
   * Names/variables in Python do not have a type. Values have types.

## Blocks and indentation

   * Python represents block structure and nested block structure with indentation, not with begin and end brackets.
   * The empty block -- Use the pass no-op statement.

### Benefits of the use of indentation to indicate structure:

   * Reduces the need for a coding standard. Only need to specify that indentation is 4 spaces and no hard tabs.
   * Reduces inconsistency. Code from different sources follow the same indentation style. It has to.
   * Reduces work. Only need to get the indentation correct, not both indentation and brackets.
   * Reduces clutter. Eliminates all the curly brackets.
   * If it looks correct, it is correct. Indentation cannot fool the reader.

