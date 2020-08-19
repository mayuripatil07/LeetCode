class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        sentence = S.split( )
        i = 0
        j = 1
        result = []
        while i < len(sentence):
            add_a = j * 'a'
            if sentence[i][0] in vowel:
                result.append(sentence[i] + 'ma' + add_a)
            else:
                result.append(sentence[i][1:] + sentence[i][0] + 'ma' + add_a)
            i += 1
            j += 1
        ans = ' '.join(result)
        return ans
                
