def appearances(s, low, high):
    if low==high:
        return {s[low] : s[low:high+1].count(s[low])}
    else:
        m = appearances(s, low+1,high)
        m[s[low]] = s[low:high+1].count(s[low])
        return m

