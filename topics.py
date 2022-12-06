from random import randint
from typing import List

# All the topics are taken from here:
# https://100ballnik.com/%d0%b4%d1%83%d1%85%d0%be%d0%b2%d0%bd%d0%be-%d0%bd%d1%80%d0%b0%d0%b2%d1%81%d1%82%d0%b2%d0%b5%d0%bd%d0%bd%d1%8b%d0%b5-%d0%be%d1%80%d0%b8%d0%b5%d0%bd%d1%82%d0%b8%d1%80%d1%8b-%d0%b2-%d0%b6%d0%b8%d0%b7/
# https://100ballnik.com/%D1%82%D0%B5%D0%BC%D1%8B-%D0%B8%D1%82%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%81%D0%BE%D1%87%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-2022-2023-%D1%81%D0%B5%D0%BC%D1%8C%D1%8F-%D0%BE%D0%B1%D1%89/
# https://100ballnik.com/%d1%82%d0%b5%d0%bc%d1%8b-%d0%b8%d1%82%d0%be%d0%b3%d0%be%d0%b2%d0%be%d0%b3%d0%be-%d1%81%d0%be%d1%87%d0%b8%d0%bd%d0%b5%d0%bd%d0%b8%d1%8f-2022-2023-%d0%bf%d1%80%d0%b8%d1%80%d0%be%d0%b4%d0%b0-%d0%b8/


def get_topics(filenames: List[str]) -> List[str]:

    result = []

    for name in filenames:
        current_topics = list(
            map(
                lambda x: x.strip(),
                open(name, "r", encoding="utf-8").readlines(),
            )
        )

        first = current_topics[randint(0, len(current_topics) - 1)]

        current_topics.remove(first)

        second = current_topics[randint(0, len(current_topics) - 1)]

        result.append(first)
        result.append(second)

    return result
