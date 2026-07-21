class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        output_array = []
        pos = 0

        for word in strs:
            if "".join(sorted(word)) in anagrams:
                output_array[anagrams["".join(sorted(word))]].append(word)
            else:
                anagrams["".join(sorted(word))] = pos
                subArray = []
                subArray.append(word)
                output_array.append(subArray)
                pos += 1
        
        return output_array