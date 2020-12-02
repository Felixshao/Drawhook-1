# usr/local/bin/python3.7
# -*-coding: utf-8 -*-

# 重构字符串
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
#
# 若可行，输出任意可行的结果。若不可行，返回空字符串。
#
# 示例 1:
#
# 输入: S = "aab"
# 输出: "aba"
# 示例 2:
#
# 输入: S = "aaab"
# 输出: ""
# 注意:
#
# S 只包含小写字母并且长度在[1, 500]区间内。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reorganize-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections


class Solution:
    def reorganizeString(self, S: str) -> str:
        a = list(S)
        b = dict(collections.Counter(a))
        max_key = max(b.items(), key=lambda x: x[1])
        if max_key[1] > (len(a) // 2) and len(a) % 2 == 0:
            return ''
        elif max_key[1] > (len(a) // 2 + 1) and len(a) % 2 == 1:
            return ''

        s: list = [max_key[0]] * int(max_key[1])
        b.pop(max_key[0])
        num = 1
        for key in b:
            for i in range(b[key]):
                s.insert(num, key)
                num += 2
                if num > len(s):
                    num = 1
        return ''.join(s)

    def reorganizeString2(self, S: str) -> str:
        a = list(S)
        b = dict(collections.Counter(a))
        c = sorted(b, key=lambda k: 0 - b[k])
        d = []
        for i in c:
            d += [i] * b[i]
        ant: list = [0] * len(d)

        ant[::2] = d[:len(ant[::2])]
        ant[1::2] = d[len(ant[::2]):]

        if ant[0] == ant[1]:
            return ""
        else:
            return "".join(ant)


if __name__ == "__main__":

    a = 'awawdddqew'
    s = Solution().reorganizeString2(a)
    print(s)