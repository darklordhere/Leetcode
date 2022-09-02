class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0     
        else:
            # Get the unique characters in the string
            set_s = set(s)
            count = 0
            for k in s:
                # If the current character is found in the unique set, remove it
                # and increase the count. 
                # Else, break and move on to the remaining subset of string
                if k in set_s:
                    set_s.remove(k)
                    count +=1
                else:
                    break
            # Using recurrsion to pass the subset of the strings and get the count
            result = [count, self.lengthOfLongestSubstring(s[1:])]
            # max of the count is the answer
            return max(result)