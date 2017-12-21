# Regular Expressions

A regular expression pattern is a sequence of characters that will match sequences of characters in a target.

The patterns or regular expressions can be defined as follows:
* Literal characters must match exactly. For example, "a" matches "a".
* Concatenated patterns match concatenated targets. For example, "ab" ("a" followed by "b") matches "ab".
* Alternate patterns (separated by a vertical bar) match either of the alternative patterns. For example, "(aaa)|(bbb)" will match either "aaa" or "bbb".
* Repeating and optional items:
  * "abc*" matches "ab" followed by zero or more occurances of "c", for example, "ab", "abc", "abcc", etc.
  * "abc+" matches "ab" followed by one or more occurances of "c", for example, "abc", "abcc", etc, but not "ab".
  * "abc?" matches "ab" followed by zero or one occurances of "c", for example, "ab" or "abc".
   
### Compiling regular expressions
When a regular expression is to be used more than once, you should consider compiling it. For example:
```
import sys, re

pat = re.compile('aa[bc]*dd')

while 1:
    line = raw_input('Enter a line ("q" to quit):')
    if line == 'q':
        break
    if pat.search(line):
        print 'matched:', line
    else:
        print 'no match:', line
```
Comments:

    We import module re in order to use regular expresions.
    re.compile() compiles a regular expression so that we can reuse the compiled regular expression without compiling it repeatedly.

### Using regular expressions

Use match() to match at the beginning of a string (or not at all).

Use search() to search a string and match the first string from the left.

Here are some examples:

>>> import re
>>> pat = re.compile('aa[0-9]*bb')
>>> x = pat.match('aa1234bbccddee')
>>> x
<_sre.SRE_Match object at 0x401e9608>
>>> x = pat.match('xxxxaa1234bbccddee')
>>> x
>>> type(x)
<type 'NoneType'>
>>> x = pat.search('xxxxaa1234bbccddee')
>>> x
<_sre.SRE_Match object at 0x401e9608>

Notes:

    When a match or search is successful, it returns a match object. When it fails, it returns None.

    You can also call the corresponding functions match and search in the re module, e.g.:

    >>> x = re.search(pat, 'xxxxaa1234bbccddee')
    >>> x
    <_sre.SRE_Match object at 0x401e9560>

    For a list of functions in the re module, see Module Contents -- http://docs.python.org/library/re.html#module-contents.

### Using match objects to extract a value

Match objects enable you to extract matched sub-strings after performing a match. A match object is returned by successful match. The part of the target available in the match object is the portion matched by groups in the pattern, that is the portion of the pattern inside parentheses. For example:

```
mo = re.search(r'height: (\d*) width: (\d*)', 'height: 123 width: 456')
mo.groups()
('123', '456')
```

## some examples
```
import re

def print_match(match):
    if match is None:
        print 'No match'
        return

    print "'{g}' was matched between the indices {s}".format(g=match.group(), s=match.span())
    return match

```
word = "infinity"


Find the character 'i' at the beginning of the word
```
  print re.findall(r"^i", word)
  ['i']

```
Find all occurrences of the character 'i'
```
print re.findall(r"i", word)
['i', 'i', 'i']
```
Find all non-overlapping two-character length substrings, where the second character is 'i'
```
print re.findall(r".i", word)
['fi', 'ni']
```

Find all non-overlapping substrings ending with character 'i',
where the preceding character exists or does not
```
print re.findall(r".?i", word)
 ['i', 'fi', 'ni']
```

Find all non-overlapping substrings 'in'
```
print re.findall(r"i[n]", word)
['in', 'in']
```
Find all non-overlapping substrings starting with character 'i',
and ending with any character except 'n'
```
print re.findall(r"i[^n]", word)
['it']
```

Perform a greedy searching for the substring starting and ending with the character 'i'
(longest possible match)
```
print_match(re.search(r"i.*i", word))
```
'infini' was matched  between the indices (0, 6)

Perform a non-greedy searching for the substring starting and ending with the character 'i'
(shortest possible match)
```
print_match(re.search(r"i.*?i", word))
'infi' was matched  between the indices (0, 4)

```

single_line = "Looks like this sentence is not as simple as it looks"



Perform a case-sensitive searching for the first occurrence of the word 'looks'
```
print_match(re.search(r"looks", single_line))

'looks' was matched  between the indices (48, 53)
```
Perform a case-insensitive searching for the first occurrence of the word 'looks'
```
print_match(re.search(r"looks", single_line, re.IGNORECASE))
'looks' was matched  between the indices (0, 5)
```

Perform a case-sensitive matching for the word 'looks'
```
print_match(re.match(r"looks", single_line))
No match
```
Perform a case-insensitive matching for the word 'looks'
```
print_match(re.match(r"looks", single_line, re.IGNORECASE))
'Looks' was matched  between the indices (0, 5)
```


# Orinoco Flow by Enya
multi_line = """Let me sail, let me sail
Let the Orinoco Flow
Let me reach, let me beach
On the shores of Tripoli"""



# Searching for the word 'sail' at the end of the string
print_match(re.search(r"sail$", multi_line))
# No match


# Searching for the word 'sail' at the end of any line
print_match(re.search(r"sail$", multi_line, re.MULTILINE))
# 'sail' was matched  between the indices (20, 24)


# Searching for the phrase 'beach On' with any character except newline between these two words
print_match(re.search(r"beach.On", multi_line))
# No match


#Searching for the phrase 'beach On' with any character between these two words
print_match(re.search(r"beach.On", multi_line, re.DOTALL))
# 'beach
# On' was matched  between the indices (67, 75)


# Searching for all the lines between the line containing the word 'reach',
# and the line ending with the word 'Tripoli'
print_match(re.search(r"^[^\n]*reach.*Tripoli$", multi_line, re.MULTILINE|re.DOTALL))
# 'Let me reach, let me beach
# On the shores of Tripoli' was matched  between the indices (46, 97)




import re


string = "Once you have accomplished small things, you may attempt great ones safely."

# Return all words beginning with letter 'a', as a list of strings
print re.findall(r"\ba[\w]+", string)
# ['accomplished', 'attempt']


# Return all words beginning with letter 'a', as an iterator yielding match objects
it = re.finditer(r"\ba[\w]+", string)
for match in it:
    print "'{g}' was found between the indices {s}".format(g=match.group(), s=match.span())
# 'accomplished' was found between the indices (14, 26)
# 'attempt' was found between the indices (49, 56)



# Split string by any character which is not a UNICODE word character
print re.split("\W+", string)
# ['Once', 'you', 'have', 'accomplished', 'small', 'things', 'you', 'may', 'attempt', 'great', 'ones', 'safely', '']

# Split string by any character which is not a UNICODE word character at most 2 split
print re.split("\W+", string, 2)
# ['Once', 'you', 'have accomplished small things, you may attempt great ones safely.']

# If the splitting pattern does not occur in the string, string is returned as the first element of the list
print re.split("(:)", string)
# ['Once you have accomplished small things, you may attempt great ones safely.']



# Replace all occurrences of space, comma, or dot with colon
print re.sub("[ ,.]", ":", string)
# Once:you:have:accomplished:small:things::you:may:attempt:great:ones:safely:

# Replace maximum 2 occurences of pattern
print re.sub("[ ,.]", ":", string, 2)
# Once:you:have accomplished small things, you may attempt great ones safely.

# Replace as 'sub', and return a tuple of (new string, number of replacements)
print re.subn("[ ,.]", ":", string)
# ('Once:you:have:accomplished:small:things::you:may:attempt:great:ones:safely:', 13)



# Find all five characthers long words
print re.findall(r"\b\w{5}\b", string)
# ['small', 'great']

# Find all five, six, or seven characthers long words
print re.findall(r"\b\w{5,7}\b", string)
# ['small', 'things', 'attempt', 'great', 'safely']

# Find all words which are at least 8 characters long
print re.findall(r"\b\w{8,}\b", string)
# ['accomplished']
