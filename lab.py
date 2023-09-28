def check(self):

    openend, closed = "([{", ")]}"

    if self[0] in closed: return False

    charDict = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    stack = []

    for charValue in self:

        if charValue in openend:
            stack.append(charValue)
        if charValue in closed:
            if charDict[charValue] != stack[-1]:
                return False
            if charDict[charValue] == stack[-1]:
                stack.pop()

    return True



paren1 = "([])"
paren2 = "[(])"
paren3 = ")("

print(check(paren3))