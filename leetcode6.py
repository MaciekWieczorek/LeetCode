import numpy as np

def convert(s, numRows):
        start = 0
        result = ""
        zigzag = []
        full = []
        
        for idx, letter in enumerate(s):
            if start == 0:
                zigzag.append(letter)
                
                if len(zigzag) == numRows:
                    full.append(zigzag)
                    zigzag= []
                    if numRows != 1:
                        start = numRows-2
                    else:
                        start = numRows-1
            else:
                for idx in range(numRows):
                    
                    if idx == start:
                        zigzag.append(letter)
                    else:
                        zigzag.append('')
                start -= 1
                
                if len(zigzag) == numRows:
                    full.append(zigzag)
                    zigzag= []
        rest = numRows - len(zigzag)
        
        print(full)

        for i in range(rest):
            zigzag.append("")
            
        full.append(zigzag)
                    
        full = np.array(full)
        full = full.T
        
        for column in full:
            for letter in column:
                result += letter
        
        return result

# s = convert("AB", 1)
# print(s)
x = 10
y = str(x)
y = y[::-1]
f = int(y)
print(f)