#leetcode 76 Hard

# Given two strings s and t, return the minimum window in s which will contain all the characters in t. --
# If there is no such window in s that covers all characters in t, return the empty string "".
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

def minWindowSubstring( s: str, t: str) -> str:
    #edge case if the input string is empty
    if t == "": return ""
    r
    # initialize hashmaps
    countT, window = {}, {}
    for c in t:
        #( to init the count of countT) if c exists in our map it will give the value stored if not it will return zero
        countT[c] = 1 + countT.get(c, 0)
    
    #need count is set to the length of the map of t
    have, need = 0, len(countT)
    #res will be pointers for the positions of the given window
    res, resLen = [-1,-1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        #add the right side of window to window hashmap

        # gets previous stored count - if not yet in window count defaults to zero
        window[c] = 1 + window.get(c, 0)

        # we want to check if c is even a key within countT
        if c in countT and window[c] == countT[c]:
            # if this is true we update the count of characrters needed to satisfy t
            have += 1
        
        while have == need:
            # update our result 
            if (r - 1 + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            # since we want it to be the smallest possible answer...
            # pop from the left of the window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            #shift from left of window to reduce window size
            l += 1
    l, r = res
    print(res)
    return s[l:r+ 1] if resLen != float("infinity") else ""
