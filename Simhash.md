## Simhash

In computer science, SimHash is a technique for quickly estimating how similar two sets are. The algorithm is used by the Google to find near duplicate webpages. We are using it as the job id to identify the near duplicate jobs. It was created by Moses Charikar.

### Explain the algorithm
- set the hashsize, ex. 64 bits, initialize them all zero
- break the phrase up into features (shingles)  
'the cat sat on the mat'  </b>
\-> {"th", "he", "e ", " c", "ca", "at", "t ",</b>
    " s", "sa", " o", "on", "n ", " t", " m", "ma"}</b>
- hash each feature using a normal 64-bit hash algorithm ex. md5</b>  
"th" -> 10010010...</b>  
"he" -> 10010110...</b>  
- set 0 to -1, sum each bit, got a sequence like : [-4 4 0 5 6 -1 -4 ...](64 bits)
- generate simhash, by setting 1: T[i]>0, 0: T[i]<0: [0 1 1 1 1 0 0 ...](64 bits)

### Make simhash
```
def make_features(input_str):
    """break the long input string into features, with length = 3
    """
    length = 3
    input_str = input_str.lower()
    out_str = re.sub(r'[^\w]+', '', input_str)
    return [out_str[i:i + length] for i in range(max(len(out_str) - length + 1, 1))]

make_features("hello world")
```
['hel', 'ell', 'llo', 'low', 'owo', 'wor', 'orl', 'rld']

```
def make_simhash(input_str):
    """make simhash from any input string"""
    features = make_features(input_str)
    return Simhash(features).value

make_simhash("hello world")
```
13548364882372308181

### Difference between two strings
calculate number of different bits from two strings
```
text_1 = "Good job"
text_2 = "Good job, Ray"

Simhash(text_1).distance(Simhash(text_2))
```
14

calculate number of different bits from two hashes
```
hash_1 = Simhash(text_1).value
hash_2 = Simhash(text_2).value

def simhash_diff(hash_1, hash_2):
    """calcuate the difference from two simhash values.
    """
    x = (hash_1 ^ hash_2) & ((1 << 64) - 1)
    ans = 0
    while x:
        ans += 1
        x &= x - 1
    return ans

simhash_diff(hash_1, hash_2)
```
14


**References**
- Google paper - [http://www.wwwconference.org/www2007/papers/paper215.pdf](http://www.wwwconference.org/www2007/papers/paper215.pdf)
- Simhash package - [https://github.com/leonsim/simhash](https://github.com/leonsim/simhash)
