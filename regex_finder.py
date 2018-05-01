import os
import re
import xml.etree.ElementTree as ET

BAD_WORDS = ['wh\w*\s?\w* the\s?\w* (\w*|\A)(fuck)(\w*|\Z)', '(\w*|\A)fuck(\w*|\Z)','(\w*|\A)dam[nm](\w*|\Z)','(\w*|\A)asshole(\w*|\Z)','(\W)ass(\W)','(\w*|\A)bitch(\w*|\Z)','(\w*|\A)shit(\w*|\Z)','(\w*|\A)dick(\w*|\Z)','(\w*|\A)douche(\w*|\Z)','(\w*|\A)piss(\w*|\Z)','(\w*|\A)pussy(\w*|\Z)','(\W)hell(\W)']

def finder(input):
    tree = ET.parse(input)
    root = tree.getroot()
    text = root[0].text
    comments = []
    swear_list = []
    context = text.split("\n")
    for line in context:
        comments.append(line)
        comments_string = "".join(comments)
    # print(comments_string)
    for swear in BAD_WORDS:
        swears = re.finditer(swear,comments_string,re.I)
        while(True):
            try:
                iter = swears.__next__()
                if re.search("(ass[^h])|(hell)",iter.group(0)) is not None:
                    start = str(iter.start()+2)
                    end = str(iter.end())
                    swear_list.append((comments_string[int(start)-1:int(end)-1], start, end))
                else:
                    start = str(iter.start()+1)
                    end = str(iter.end()+1)
                    swear_list.append((comments_string[int(start)-1:int(end)-1], start, end))
            except StopIteration:
                break
    return swear_list
    # return text
print(finder("goldstandard2008-1.xml"))
