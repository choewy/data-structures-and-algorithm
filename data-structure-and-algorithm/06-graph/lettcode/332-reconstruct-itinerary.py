from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        temp = []

        for [_from, _to] in tickets:
            if _from not in temp:
                temp.append(_from)

            if _to not in temp:
                temp.append(_to)

        maps = {ticket: [] for ticket in temp}

        for [_from, _to] in tickets:
            maps[_from].append(_to)

        for path in temp:
            maps[path] = sorted(maps[path], reverse=True)

        def recursive(path):
            while maps[path]:
                to = maps[path].pop()
                recursive(to)
            res.append(path)

        res = []
        recursive('JFK')
        return res[::-1]


if __name__ == "__main__":
    solution = Solution()

    # TEST CASE 1
    print(solution.findItinerary([
        ["JFK", "KUL"],
        ["JFK", "NRT"],
        ["NRT", "JFK"]
    ]) == ["JFK", "NRT", "JFK", "KUL"])

    # TEST CASE 2
    print(solution.findItinerary([
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"]
    ]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])

    # TEST CASE 3
    print(solution.findItinerary([
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["LHR", "SFO"]
    ]) == ["JFK", "MUC", "LHR", "SFO", "SJC"])

    # TEST CASE 4
    print(solution.findItinerary([
        ["EZE", "TIA"],
        ["EZE", "HBA"],
        ["AXA", "TIA"],
        ["JFK", "AXA"],
        ["ANU", "JFK"],
        ["ADL", "ANU"],
        ["TIA", "AUA"],
        ["ANU", "AUA"],
        ["ADL", "EZE"],
        ["ADL", "EZE"],
        ["EZE", "ADL"],
        ["AXA", "EZE"],
        ["AUA", "AXA"],
        ["JFK", "AXA"],
        ["AXA", "AUA"],
        ["AUA", "ADL"],
        ["ANU", "EZE"],
        ["TIA", "ADL"],
        ["EZE", "ANU"],
        ["AUA", "ANU"]
    ]) == [
        "JFK", "AXA", "AUA", "ADL", "ANU", "AUA", "ANU", "EZE", "ADL", "EZE", "ANU",
        "JFK", "AXA", "EZE", "TIA", "AUA", "AXA", "TIA", "ADL", "EZE", "HBA"
    ])
