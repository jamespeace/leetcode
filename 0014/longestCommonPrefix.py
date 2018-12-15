#!/usr/bin/env python3
class Soluion:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        >>> s = Solution()
        >>> l = ["flower", "flow", "flight"]
        >>> s.longestCommonPrefix(l)
        'fl'
        """
        count = len(strs)
        common_prefix = ""
        for i in range(min([len(l) for l in strs])):
            current_word = strs[0][i]
            for j in range(1, count):
                if strs[j][i] != current_word:
                    return common_prefix
            common_prefix += current_word
        return common_prefix