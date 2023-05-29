from queue import PriorityQueue


class Worker:

    def __init__(self) -> None:
        self.friend = None
        self.counter = 0

    def work(self):
        self.counter += 1

    def is_done(self):
        return self.friend is not None and \
            self.counter >= ord(self.friend) - 4

    def is_empty(self):
        return self.friend is None

    def release(self):
        cur = self.friend
        self.friend = None
        return cur

    def grab(self, new_friend):
        self.friend = new_friend
        self.counter = 0


class WorkerHandler:

    def __init__(self, n_workers, reqs) -> None:
        self.workers = [Worker() for _ in range(n_workers)]
        self.pq = PriorityQueue()
        self.reqs = self.load_reqs(reqs)
        self.refill_queue()

    def load_reqs(self, path):
        with open(path) as f:
            reqs = {}
            for row in f:
                a, b = row.strip().split()
                if b not in reqs:
                    reqs[b] = set()

                if a not in reqs:
                    reqs[a] = set()

                reqs[b].add(a)
        return reqs

    def remove_dependency(self, friend):
        for v in self.reqs.values():
            v.discard(friend)

    def refill_queue(self):
        for k, v in tuple(self.reqs.items()):
            if not v:
                self.pq.put(k)
                del self.reqs[k]

    def refill_workers(self):
        for worker in self.workers:
            if worker.is_empty() and self.pq.qsize() > 0:
                worker.grab(self.pq.get())

    def empty_done_workers(self):
        for worker in self.workers:
            if worker.is_done():
                cur = worker.release()
                print(cur)
                self.remove_dependency(cur)

        self.refill_queue()

    def work_all(self):
        for worker in self.workers:
            worker.work()

    def is_finish(self):
        return all((w.is_empty() for w in self.workers)) and \
                len(self.reqs) == 0 and \
                self.pq.qsize() == 0
