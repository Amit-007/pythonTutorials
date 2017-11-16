from collections import deque
queue = deque(["Eric", "Sean", "Adam", "Michele", "Jenny"])
queue.append("Amit")
queue.append("Bittu")
queue.append("Graham")

print(queue)


queue.popleft()
print(queue)

queue.popleft()
print(queue)

