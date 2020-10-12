# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다. 
# 입력: "A man, a plan, a canal: Panama"
# 출력: true
import collections

def isPalindrome(s):

    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

# print(isPalindrome('abannmn'))