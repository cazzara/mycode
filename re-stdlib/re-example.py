"""
Using Regular Expressions in Python via the re module
Author : Chris Azzara
"""

import re

"""
Regular Expression Metacharacters:
. ^ $ * + ? { } [ ] \ | ( )

(1) [] -- Specifies a character class
    [abc] -- matches a, b, or c
    [a-c] same as above

    Metacharacters are not active inside classes*
    [akm$] -- matches a, k, m, or $

    Including the ^ as the first character in a class will complement that class
    [^5] -- matches any character except 5

(2) \ -- The escape character
    Backslash escapes other metacharacters
    \\ -- matches a \
    \[ -- matches a [
    \? -- matches a ?
    etc ...

    Some special character classes are specified by using backslash:
    \w -- matches any alphanumeric character, same as [a-zA-Z0-9_]
    \W -- matches any NON alphanumeric character, same as [^a-zA-Z0-9_]
    \s -- matches any whitespace character
    \S -- matches any NON whitespace character
    \d -- matches any digit, same as [0-9]
    \D -- matches any NON digit, same as [^0-9]

    [\s,.] -- matches any whitespace , or .
    
(3) . -- The Dot
    Matches any character (except a newline, unless re.DOTALL flag is given)

(4) * -- The Splat
    Matches the preceeding character ZERO or more times
    ca*t -- matches ct, cat, caaat, etc

(5) + -- The Plus
    Requires at least one occurence of the preceeding character
    ca+t -- matches cat, caaat, but will NOT match ct

(6) ? -- The ?
    Matches the preceeding character ZERO or ONCE
    home-?brew -- matches home-brew or homebrew

(7) {m, n} -- Repeaters m,n are integers
    At least m copies and at most n copies of the preceeding character
    a/{1,3}b -- matches a/b, a//b, a///b but NOT a////b or ab
    {m}  Requires exactly m copies of the preceeding character
    a/{3}b  --  matches a///b

(8) () -- Grouping Characters
    Contains a match group which can be used to further extract text contents
    the match object has a group() method which can index into specific groups
    group(0) is the whole match
    group(1) is the first group and so on

"""

# Compiling a Regular Expression:
pattern = re.compile(r"ca*t", re.IGNORECASE)

s = "caaaaat"


"""
Important re methods:
match()  --  Determine if re matches at beginning of the string (implied caret)
search() --  Determine if re matches anywhere in the string (no implied caret)
findall() -- Find all substrings that match re and return as a list
finditer() -- Find all substrings that match re and return as iterator
"""
# Now we have a "match" object
m = re.search(pattern, s)
# Alternate method:
# m = pattern.search(s)
print(m)

"""
Methods availble on match objects:
group()  -- Return the string matched by the RE
            Or if you have multiple groups in your RE using ()
            you can specify the index of the group with group(0) being all
start() -- Starting position of the match
end()   -- Ending position of the match
span()  -- Tuple containing start and end positions
"""

# Common usage of matching
s = "123 xyz !@#"
p = re.compile(r"\s\w{3}\s")
match = p.search(s)
if match:
    print("Found!")
    print(match.group())
else:
    print("No Match :(")

p  = re.compile(r"\d+")
s = "12 drummers drumming, 11 pipers piping, 10 lords a-leaping"
# Return first match
m = p.search(s)
print(m)
# Return list of string matches
m = p.findall(s)
print(m)
# Return iterator of match objects
m = p.finditer(s)
for match in m:
    print(match)
