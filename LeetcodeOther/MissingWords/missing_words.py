

def missingWords(s, t):
    res = []
    t_words = t.split()
    s_words = s.split()
    size = len(s_words)
    i = 0
    j = 0
    for j in range(size):
        if s_words[j] == t_words[i]:
            i += 1
            if i >= len(t_words):
                break
        else:
            res.append(s_words[j])
    for k in range(j+1, size):
        res.append(s_words[k])
    return res


s1 = " I am using computer to improve my work"
t1 = "am computer to improve"
print(missingWords(s1, t1))
