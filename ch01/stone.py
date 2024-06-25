def is_even(n):
    return n % 2 == 0

def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n - 1)

def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1)
        
play_alice(20)