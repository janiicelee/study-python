#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
#paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#banned = ["hit"]
#출력
# "ball"
import collections
import re

def mostCommonWord(paragraph: str, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    print(words)

    counts = collections.Counter(words)
    print(counts)
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))