def f(palindrome):
    for i in range(len(palindrome)):
        if palindrome[i]!=palindrome[len(palindrome)-1-i]:
            return False
    return True

print(f("kajaki"))