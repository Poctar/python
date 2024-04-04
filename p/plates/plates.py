def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 2 ~ 6 char OK?
    if 2 <= len(s) <= 6 and s.isalnum():
        # all string OK?
        if s.isalpha():
            return True
        # NOT all string
        else:
            if s.isdigit():
                return False
            # first 2 char string AND last char number?
            if s[:2].isalpha and s[-2:].isdigit():
                for i in range(len(s)):
                    # char is number?
                    if s[i].isdigit():
                        # start with 0 OR end with string?
                        if s[i] == "0" or s[i:].isalpha():
                            return False
                        else:
                            return True
            # NOT first 2 char string AND last char number
            else:
                return False
        return False
    # NOT 2 ~ 6 char OK?
    else:
        return False

main()

# if 2 ~ 6 char
#     if all string
#         True
#     otherwise
#         if all number
#             False
#         if first 2 char string AND last char number
#             read one char each
#                 if one char us number
#                     if one char start with 0 OR end with string
#                         False
#                     otherwise
#                         True
#         otherwise
#             False
#         False
# otherwise
#     False

