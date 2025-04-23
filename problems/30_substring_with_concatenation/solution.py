class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = {}
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        for i in range(len(s) - total_len + 1):
            current_count = {}
            j = 0
            
            while j < len(words):
                word = s[i + j * word_len:i + (j + 1) * word_len]
                
                if word not in word_count:
                    break
                    
                current_count[word] = current_count.get(word, 0) + 1
                
                if current_count[word] > word_count[word]:
                    break
                    
                j += 1
            
            if j == len(words):
                result.append(i)
        
        return result

if __name__ == "__main__":
    solution = Solution()
    
    s1 = "barfoothefoobarman"
    words1 = ["foo","bar"]
    print(solution.findSubstring(s1, words1))
    
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    print(solution.findSubstring(s2, words2))
    
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar","foo","the"]
    print(solution.findSubstring(s3, words3)) 