#문자열 배열을 받아 애너그램 단위로 그룹핑
#입력
#["eat", "tea", "tan", "ate", "nat", "bat"]
#출력
#[
#    ["ate", "eat", "tea"],
#    ["nat", "tan"],
#    ["bat"]
#]

import collections

def groupAnagrams(strs:[str]):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        print(word)

    return anagrams.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))