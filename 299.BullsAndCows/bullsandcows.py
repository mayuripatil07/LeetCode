from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count=collections.Counter(secret)
        guess_count=collections.Counter(guess)
        A,B=0,0
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                A+=1
                guess_count[guess[i]]-=1
                secret_count[guess[i]]-=1
            elif guess[i] not in secret_count:
                guess_count[guess[i]]=0
        for key,value in guess_count.items():
                B+=min(secret_count[key],value)
        return str(str(A)+'A'+str(B)+'B')
