class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result=[]
        n=len(products)
        prefix=""
        bsStart=0

        for c in searchWord:
            prefix+=c
            start=bisect_left(products,prefix,bsStart,n)
            result.append([])

            for i in range(start,min(start+3,n)):
                if products[i].startswith(prefix):
                    result[-1].append(products[i])
            
            bsStart=start
        return result
