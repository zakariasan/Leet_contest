def is_palindrome(s: str) -> bool:
    for i in range(len(s)):
        if s[i] != s[-i + len(s) - 1]:
            return False
    return True


def palindrome_partitioner(s: str) -> int:
    if (is_palindrome(s)):
        return 0
    if len(set(s)) == len(s):
        return len(s) - 1
    else:
        cnt = 0
        st = ''
        for nb, item in enumerate(s):
            if is_palindrome(s[nb + 1:]) and is_palindrome(s[:nb]):
                cnt += 1
        return cnt
    

print(palindrome_partitioner("aabaacd"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))
