import json, requests
""" 
I am not sure about how to define this semantic duplicates function.
So for two given strings I have implemented this function.

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


"""
def ifSubstring(s1, s2):
    if s1.find(s2) == -1 or s2.find(s1) == -1:
        return False
    else:
        return True    

def check_semantic_duplicates(data, types):
    pass
        
def showData(data, types):
    for item in data[types]:
        s = item["confName"] + " "+ item["confStartDate"] + " " + item["city"] + "," + item["country"] + " " + item["entryType"] + " " + item["confUrl"]
        print(s)

def check_exact_duplicate(data, type):
    d = {}
    ans = []
    for item in data[type]:
        s = item["confName"] + " "+ item["confStartDate"] + " " + item["city"] + "," + item["country"] + " " + item["entryType"] + " " + item["confUrl"]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    for i in list(d.keys()):
        if d[i] > 1:
            ans.append(i)        
        
    print(*ans, sep="\n")


if __name__ == "__main__":
    req = requests.get("https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences")

    req_text = req.text

    data = json.loads(req_text)
    
    showData(data, "paid")
    
    check_exact_duplicate(data, "paid")