def appearances(s, low, high):
    if low>high:
        return {}
    else:
        m = appearances(s, low+1,high)
        if s[low] in m:
            m[s[low]] += 1
        else:
            m[s[low]] = 1
        return m

