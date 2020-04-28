# JSON-Simplify
Convert JSON to human readable Data

I have defined total two functions where one could print all the relevant data from the JSON as human readable data.
The second method is where the function will detect the exact duplicate entries in the JSON.

# Semantic Duplicate

I am not sure about how to define this semantic duplicates function.
So for two given strings I have implemented this function.

```
def ifSubstring(s1, s2):
    if s1.find(s2) != -1 or s2.find(s1) != -1:
        return True
    else:
        return False  

def check_semantic_duplicates(s1, s2):
    l1 =s1.split()
    l2 = s2.split()
    flag = False
    n = len(l1)
    m = len(l2)
    if n >= m:
        for i in range(n):
            for j in range(m):
                if ifSubstring(l1[i], l2[j]):
                    flag = True
    else:
        for i in range(m):
            for j in range(n):
                if ifSubstring(l2[i], l1[j]):
                    flag = True
    return flag                


s2 = "React Conference"
s1 = "ReactConf"
print(check_semantic_duplicates(s1, s2))
```
