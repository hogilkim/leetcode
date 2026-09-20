# asdfbar
#     ${asdf}${foo}
#     i


def function(inputstr, dictionary):

    start = -1
    end = -1
    res = ""
    i = 0
    while i < len(inputstr):
        # print(i, inputstr)
        if inputstr[i] == "$" and i < len(inputstr) - 1 and inputstr[i + 1] == "{":
            start = []

        if inputstr[i] == "}" and start != -1:
            end = i

        # substring insdie the braces
        if start != -1 and end != -1:
            # check if the substring is in the dictionary
            substring = inputstr[start + 2 : end]
            # if there is, substitte
            if substring in dictionary:
                inputstr = (
                    inputstr[:start] + dictionary[substring] + inputstr[end + 1 :]
                )
                i = start + len(substring) - 1

            start = -1
            end = -1

        i += 1
    print(inputstr)
    return inputstr


# def function(inputstr, dictionary):

#     start = -1
#     end = -1
#     res = ""
#     for i in range(len(inputstr)):

#         if inputstr[i] == "$" and i < len(inputstr) - 1 and inputstr[i + 1] == "{":
#             start = i

#         if inputstr[i] == "}" and start != -1:
#             end = i
#         if start == -1:
#             res += inputstr[i]

#         # substring insdie the braces
#         if start != -1 and end != -1:
#             # check if the substring is in the dictionary
#             substring = inputstr[start + 2 : end]

#             if substring in dictionary:
#                 res += dictionary[substring]
#             start = -1
#             end = -1
#     return res


# def function(inputstr, dictionary):

#     start = -1
#     end = -1
#     res = ""
#     for i in range(len(inputstr)):
#         res += inputstr[i]
#         if inputstr[i] == "$" and i < len(inputstr) - 1 and inputstr[i + 1] == "{":
#             start = i

#         if inputstr[i] == "}" and start != -1:
#             end = i

#         # substring insdie the braces
#         if start != -1 and end != -1:
#             # check if the substring is in the dictionary
#             substring = inputstr[start + 2 : end]
#             # o${2}
#             # 01234
#             # 0s23e
#             #
#             if substring in dictionary:
#                 distance = end - start + 1
#                 res = res[:-distance] + dictionary[substring]
#                 print(res)
#             start = -1
#             end = -1
#     print(res)
#     return res


assert function("${1}${2}asdf", {"1": "one", "2": "two"}) == "onetwoasdf"
assert function("${1}${2}asdf", {"1": "o", "2": "two"}) == "otwoasdf"

assert function("asdf${foo}", {"foo": "bar"}) == "asdfbar"
assert function("${1}${2}asdf", {"1": "oneone", "2": "twotwo"}) == "oneonetwotwoasdf"
