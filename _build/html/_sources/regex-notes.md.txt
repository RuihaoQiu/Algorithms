
## Regex notes

This is a personal regex note for daily work, will keep update.


```python
import re
```

### re module

- re.match(*pattern*, *string*) - if zero or more characters **at the beginning of** *string* match the regular expression *pattern*, return a corresponding match object.
```
## match
re.match(r"project", "project manager")
```
<\_sre.SRE_Match object; span=(0, 7), match='project'>
```
## not match
re.match(r"manager", "project manager")
```

- re.search(*pattern*, *string*) - go through the whole *string*, look for the first location where the regular expression *pattern* produces a match.
```
## use search
re.search(r"manager", "project manager")
```
<\_sre.SRE_Match object; span=(8, 15), match='manager'>


- re.complie(*pattern*) - compile a regular expression *pattern* into a regular expression object, then we can use search, match and other methods. More efficient when the expression will be used several times.
```
## match again
regex = re.compile(r"project")
regex.match("project manager")
```
<\_sre.SRE_Match object; span=(0, 7), match='project'>


- re.split(*pattern*, *string*) - split *string* by the occurrences of *pattern*. If parentheses are used in *pattern*, then the text of the pattern are also returned as part of the resulting list.
```
## split
re.split(r' ', 'project manager, IT section')
```
['project', 'manager,', 'IT', 'section']
```
## split with more characters
re.split(r'[ ,]+', 'project manager, IT section')
```
['project', 'manager', 'IT', 'section']
```
## split with parentheses
re.split(r'([ ,]+)', 'project manager, IT section')
```
['project', ' ', 'manager', ', ', 'IT', ' ', 'section']


- re.sub(*pattern*, *repl*, *string*) - replace the matches in *string* with *repl*.
```
## remove any of the special characters
re.sub(r"[,\.\:\;\!]+", "", "project manager, IT section...")
```
'project manager IT section'


- re.findall(*pattern*, *string*) - find all non-overlapping matches of *pattern* in *string*, return as a list of strings.
```
## find all special character in the pattern
re.findall(r"[,\.\:\;\!]+", "project manager, IT section...")
```
[',', '...']


### Special characters
\.   
Matches any character except a newline.

\^  
Matches the start of the string.

\$  
Matches the end of the string.

\*  
Match 0 or more repetitions. ab* will match 'a', 'ab', or 'abbbb' (any number of 'b's).

\+  
Match 1 or more repetitions. ab+ will match 'ab', or 'abbbb' (any number of 'b's), not 'a'.

\?  
Match 0 or 1 repetitions. ab? will match 'a' or 'ab', useful for plural form, birds? will match both 'bird' and 'birds'.

\*?, +?, ??  
Match as much text as possible.

\\  
Either escapes special characters (permitting you to match characters like '\*', '?', and so forth), or signals a special sequence; special sequences are discussed below.

\[\]  
[abc] will match any of 'a', 'b', or 'c'.
[a-z] will match any lowercase ASCII letter.
Special characters lose their special meaning inside sets. [(\+\*)] will match any of the literal characters '(', '+', '\*', or ')'.

\|  
A|B will match either A or B. An arbitrary number of REs can be separated by the '|' in this way, run from left to right, once A matches, B will not be tested further.

\b  
Matches the word boundary.

\d  
Matches any Unicode decimal digit, equivalent to [0-9]

\s  
Matches Unicode whitespace characters (which includes [ \t\n\r\f\v])

\w  
For Unicode (str) patterns:
Matches Unicode word characters, equivalent to [a-zA-Z0-9_].

### Example
```
def clean(str_input):
    """Clean input string by keeping only Unicode ([a-zA-Z0-9_]) patterns and dot(.)

    input
    --------
    str_input : string
        any type of string

    output
    --------
    str_clean : string
        lower case string without any special characters in the pattern.

    notes
    --------
    - clean string
    - remove multiple spaces
    - lower case
    """
    sep = re.compile(r"[^\w.]")
    try:
        str_clean = sep.sub(" ", str_input)
        str_clean = re.sub("\s+", " ", str_clean).strip()
        return str_clean.lower()
    except:
        return ""
```
```
clean("fwoejurw#5r[x]few2\.3540#%###&^^*}$%$#&%*&(!)")
```
'fwoejurw 5r x few2 .3540'
