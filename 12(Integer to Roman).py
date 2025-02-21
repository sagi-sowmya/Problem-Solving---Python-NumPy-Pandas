class Solution:
    def intToRoman(self, num: int) -> str:
        #n=len(str(num))
        roman_str=[]
        Roman_list=[("I",1),("IV",4),("V",5),("IX",9),("X",10),("XL",40),("L",50),("XC",90),("C",100),("CD",400),("D",500),("CM",900),("M",1000)]
        for symbol,value in reversed(Roman_list):
            if num==0:
                break
            count,num=divmod(num,value)
            roman_str.append(symbol*count)
        return "".join(roman_str)        

solution=Solution()
num=3749
print("Roman equivalent:",solution.intToRoman(num))        