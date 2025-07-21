class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_string=[]
        for char in s:
            if len(fancy_string)>=2 and\
               fancy_string[-1] == char and\
               fancy_string[-2] == char:
               continue
            else:
               fancy_string.append(char)

        return"".join(fancy_string)