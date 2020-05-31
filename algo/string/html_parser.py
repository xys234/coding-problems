"""

1410.
Medium

"""


import re

class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": '&',
            "&gt;": '>',
            "&lt;": '<',
            "&frasl;": '/'
        }
        
        # https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s15.html
        regex = re.compile("|".join(map(re.escape, entities.keys())))

         # For each match, look up the corresponding value in the dictionary
        return regex.sub(lambda match: entities[match.group(0)], text)