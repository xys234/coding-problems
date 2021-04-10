"""

443.
Medium

Amazon DS

"""



class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        start = 0  # write position
        prev = chars[0]
        length = 1
        
        i = 1
        while i < n:
            curr = chars[i]
            if curr != prev:
                if length > 1:
                    s = [prev] + list(str(length))
                    write_length = len(s)
                    for j, w in enumerate(s):
                        chars[start + j] = w
                else:
                    chars[start] = prev
                    write_length = 1
                start += write_length
                length = 1
                
            else:
                length += 1
            
            prev = curr
            i += 1
        
        if length == 1:
            chars[start] = prev
            start += 1
        else:
            s = [prev] + list(str(length))
            for j, w in enumerate(s):
                chars[start + j] = w
            start += len(s)
            
        # print(chars)
        return start
    
    def compress2(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write