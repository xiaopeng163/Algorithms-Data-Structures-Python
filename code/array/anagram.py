def is_anagram(s1, s2):
    
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2
