#!/use/bin/python3
""" print the texts!"""


def text_indentation(text):
    """ printing Text """
    i = 0
        
    while i < len(text):
        if text[i] in [":",".","?"]:
            print("{:s}\n".format(text[i]).lstrip())
            i += 1
            if i < len(text):
                if text[i] == " ":
                    i += 1
        else:
            print("{:s}".format(text[i]), end="")
            i += 1
