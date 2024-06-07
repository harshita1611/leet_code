class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()
        result = []

        for i in words:
            for j in range(len(i)+1):
                prefix=i[:j]
                if prefix in roots:
                    result.append(prefix)
                    break
            else:
                result.append(i)
        
        return ' '.join(result)
