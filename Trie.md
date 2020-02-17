## Trie
A trie is a tree-like data structure whose nodes store the letters of an alphabet.
It is super powerful for some tasks like autocomplete and feature extraction in ML applications.

```
import re
from pytrie import StringTrie
```

### Autocomplete
Suggest the complete word/phrase for any prefix input.

```
def suggest(input_str, key_trie, top_n=10):
    """autocomplete the input_str, show the top_n suggestions with highest score
    """
    input_low = input_str.lower()
    out_items = key_trie.items(prefix=input_low)
    out_sort = sorted(out_items, key=lambda tup: tup[1], reverse=True)
    out_list = [i for i,v in out_sort[:top_n]]
    return out_list
```

**Simple example**
```
key_dict =  dict({"hello":10, "dog":3, "hell":20, "cat":3, "h":4,  
        "hel":15, "help":33, "helps":47, "helping":40})
key_trie = StringTrie(key_dict)
suggest("hel", key_trie)
```
['helps', 'helping', 'help', 'hell', 'hel', 'hello']

**Practical example - location autocomplete**  
Work with world cities data, [find here](https://simplemaps.com/data/world-cities)
```
import pandas as pd
input_file = "data/worldcities.xlsx"
input_df = pd.read_excel(input_file)
```

make trie structure
```
def make_trie(input_df):
    input_df["fullname"] = input_df[["city", "admin_name", "country"]].apply(lambda x: ', '.join(x.astype(str).str.lower()), axis=1)
    input_df["population"] = input_df["population"].fillna(0)
    out_dict = dict(zip(input_df.fullname.str.lower(), input_df.population))
    return StringTrie(key_dict)

key_trie = make_trie(input_df)
```

```
suggest("par", key_trie, top_n=5)
```
['paris, île-de-france, france',<br/>
 'parbhani, mahārāshtra, india',<br/>
 'paraná, entre ríos, argentina',<br/>
 'paramaribo, paramaribo, suriname',<br/>
 'paradise, nevada, united states']<br/>
*(**find city called 'paradise' in US)*

```
suggest("sha", key_trie, top_n=5)
```
['shanghai, shanghai, china',<br/>
 'shangqiu, henan, china',<br/>
 'shantou, guangdong, china',<br/>
 'shangrao, jiangxi, china',<br/>
 'sharjah, ash shāriqah, united arab emirates']

```
suggest("ber", key_trie, top_n=5)
```
['berlin, berlin, germany',<br/>
 'bern, bern, switzerland',<br/>
 'bertoua, est, cameroon',<br/>
 'bergen, hordaland, norway',<br/>
 'bergamo, lombardy, italy']

To be notice, here we use the population as the score to sort the suggestions. What need to be improved is just to re compute the scores by consider more factors.


### Feature extraction
When we want to search a large amount of keywords from one/many text. Trie structure become super powerful. It is the opposite way to implement the Trie from above.

Import a script `Trie.py`, which you can find [here](https://gist.github.com/EricDuminil/8faabc2f3de82b24e5a371b6dc0fd1e0), also feel free to use other packages.
```
from Trie import Trie
```

**Make regex from trie**
```
text = """Amsterdam - Van Gogh Museum
Paris –  Eiffel tower, Louvre Museum
Munich – Oktoberfest
Berlin – Zoo etc."""
```

```
def make_regex(input_list):
    """Build regex from trie structure.
    """
    t = Trie()
    for w in input_list:
        t.add(w)
    regex = re.compile(r"\b" + t.pattern() + r"\b", re.IGNORECASE)
    return regex
```
**Small key set**
```
small_keys = ["munich", "paris", "berlin", "brussels"]
regex = make_regex(small_keys)
```
```
%%time
regex.findall(text)
```
CPU times: user 14 µs, sys: 0 ns, total: 14 µs<br/>
Wall time: 17.9 µs<br/>
['Paris', 'Munich', 'Berlin']

**Large key set**
```
large_keys = input_df.city.values
print(len(large_keys))
regex_large = make_regex(large_keys)
```
15493

```
%%time
regex_large.findall(text)
```
CPU times: user 64 µs, sys: 1e+03 ns, total: 65 µs<br/>
Wall time: 67.7 µs<br/>
['Amsterdam', 'Van', 'Paris', 'Munich', 'Berlin']

Super fast! However, we have a wrong result Van, which is not a city. To avoid this ambiguity, more sophistical methods are required.

**References**
- Intro to Trie: [https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
- pytrie package: [https://pytrie.readthedocs.io/en/latest/](https://pytrie.readthedocs.io/en/latest/)
- Trie script: [https://gist.github.com/EricDuminil/8faabc2f3de82b24e5a371b6dc0fd1e0](https://gist.github.com/EricDuminil/8faabc2f3de82b24e5a371b6dc0fd1e0)
- City data : [https://simplemaps.com/data/world-cities](https://simplemaps.com/data/world-cities)
