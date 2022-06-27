
#Example 1:

#Input: s = "III"
#Output: 3
#Explanation: III = 3.



#Example 2:

#Input: s = "LVIII"
#Output: 58



def romanToInt(s):
    roman={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    for i in range(len(s)):
        if i + 1 < len (s) and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]  
        else:
            res += roman[s[i]]   

    return res


print(romanToInt("VI"))

