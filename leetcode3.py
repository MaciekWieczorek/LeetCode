def lengthOfLongestSubstring(s: str) -> int:
        diff_values = []
        best = 0
        for n in s:
            if n not in diff_values:
                diff_values.append(n)
            else:    
                found = False
                for idx, k in enumerate(diff_values):
                    if found == False:
                        if k == n:
                            diff_values = diff_values[idx+1:]
                            found = True
                            diff_values.append(n)
            if len(diff_values) > best:
                best = len(diff_values)
                print(diff_values)
            
        return best

def test(s):
    print(s)
    print(s[0+1:])

print(lengthOfLongestSubstring('aabaab!bb'))
test([1,2,3,4])