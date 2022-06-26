def bananas(s):
    TARGET = "banana"

    def banana(s, iS=0, iT=0, ans=set()):
        if len(TARGET) - (iT + 1) <= len(s) - (iS + 1) and iT < len(TARGET) and iS < len( s):
            if TARGET[iT] == s[iS]:
                if iT == len(TARGET) - 1:
                    ans.add(''.join(s[:iS + 1] + ['-'] * (len(s) - (
                                iS + 1))))
                ans |= banana(s.copy(), iS + 1, iT + 1)

            s[iS] = '-'
            ans |= banana(s, iS + 1, iT)
        return ans

    return banana(list(s))

generateRndChar = lambda n: ["b", "n", "a"][(n < 50) + (n < 80)]


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}