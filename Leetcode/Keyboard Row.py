class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        retwords = []
        qline = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        aline = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        zline = ['Z', 'X', 'C', 'V', 'B', 'N', 'M',
                 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        inqline = False
        inaline = False
        inzline = False
        for word in words:
            inqline = False
            inaline = False
            inzline = False
            if word[0] in qline:
                inqline = True
                for chword in word:
                    if chword not in qline:
                        inqline = False
            elif word[0] in aline:
                inaline = True
                for chword in word:
                    if chword not in aline:
                        inaline = False
            else:
                inzline = True
                for chword in word:
                    if chword not in zline:
                        inzline = False
            if inqline or inaline or inzline:
                retwords.append(word)
        return retwords


if __name__ == '__main__':
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
