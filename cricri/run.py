from queue import PriorityQueue


with open('input.txt') as f:
    reqs = {}
    for row in f:
        a, b = row.strip().split()
        if b not in reqs:
            reqs[b] = set()

        if a not in reqs:
            reqs[a] = set()

        reqs[b].add(a)


pq = PriorityQueue()


def remove_dependency(friend):
    for v in reqs.values():
        v.discard(friend)


def refill_queue():
    for k, v in tuple(reqs.items()):
        if not v:
            pq.put(k)
            del reqs[k]


friend_count = len(reqs)
ans = ""

while friend_count:
    refill_queue()
    cur = pq.get()
    ans += cur
    remove_dependency(cur)
    friend_count -= 1

print(ans)
