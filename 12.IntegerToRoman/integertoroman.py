class Solution:
    def intToRoman(self, num: int) -> str:
        hmap = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        s = ""
        i = 0
        num_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while(i < len(num_list)):
            if num - num_list[i] < 0:
                i += 1
            else:
                diff = num - num_list[i]
                s += hmap[num_list[i]]
                num = diff
        return s
