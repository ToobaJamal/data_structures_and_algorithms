import time

def recursive_countdown_timer(n):
  if n == 0:
    return n
  else:
    print(n)
    time.sleep(1) # 1 second delay
    return recursive_countdown_timer(n-1)
