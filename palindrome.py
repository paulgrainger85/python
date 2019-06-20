def checkIfPalindrome(s, allPerms = False):
    '''
    @allPerms = False
     if the user just passes in a string, we simply check if the string is the same backwards as it is forwards
     otherwise we go into the below logic
    
    @allPerms = True
     I'm going to say that the string s can be represented as a palindrome if:
     for a string of even length, the count of each distinct character is divisble by 2
     for a string of odd length, the count of each distinct character -1 are divisble by 2
    '''
    if len(s) == 1:
        print(f'{s} is only 1 character')
        return False
    
    if not allPerms:
        return s == s[::-1]

    l = list(map(lambda n: s.count(n) % 2 , set(s)))
    isPalindrome = False

    # for a string of even length we just need every character to be divisble by 2
    if len(s) % 2 == 0:
        isPalindrome = len(l)*[0]  == l
    else:
        try:
            l.pop(l.index(1))
            isPalindrome = len(l)*[0] == l
        except: # we can just do nothing here as if the above fails due to no odd values, then not a palindrome
            pass
            
    return isPalindrome

