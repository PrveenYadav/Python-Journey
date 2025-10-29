# Problem: Encode and Decode Strings

# tomorrow is the day -> Sunday : And you have to revise all prev DSA Problems 
# And Do - Honest - DSA : Make Notes : Proper DRY RUN : START BACKEND

class Solution:
    def __init__(self):
        pass
        
    # Problem: Encode and Decode Strings => Time: O(m), Space: O(m+n)
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


if __name__ == "__main__":
    myObj = Solution()
    strs = ["write","code","like","genius"]

    print("\nOriginal strings: ", strs)
    print("Encoded String: ", myObj.encode(strs))
    encodedVal = myObj.encode(strs)
    print("Decoded String: ", myObj.decode(encodedVal), "\n")