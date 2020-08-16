class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for i in range(len(searchWord)):
            word = searchWord[:i+1]
            res = []
            for j in range(len(products)):
                if products[j].startswith(word):
                    if len(res) < 3 and j <= len(products):
                            res.append(products[j])
            result.append(res)

        return result
            
