class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        res = 0
        punc = ['.', ',', '!']
        for w in words:
            if len(w) == 1:
                if w.isalpha() or w in punc: res+=1
                continue
            if w[0] == '-' or w[-1] == '-': continue
            n_hyphen = 0
            for i, ch in enumerate(w):
                if i != len(w) -1 and ch in punc : break
                if ch == '-' :
                    if w[max(0, i-1)] in punc or w[min(len(w)-1, i+1)] in punc: break
                    else: n_hyphen+=1
                if n_hyphen > 1: break
                if ch.isdigit(): break
            else:
                res+=1
        return res
            
        