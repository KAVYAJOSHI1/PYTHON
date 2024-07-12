def count(s: str) -> int:
    words=s.strip().split()
    return len(words)
print("ENTER THE STRING")
s=input()
print("THE WORD COUNT OF THE STRING IS ",str(count(s)))