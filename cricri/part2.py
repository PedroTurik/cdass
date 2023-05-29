from worker import WorkerHandler


worker_handler = WorkerHandler(5, "input.txt")


seconds = 0

worker_handler.refill_queue()

while not worker_handler.is_finish():

    worker_handler.refill_workers()

    worker_handler.work_all()

    worker_handler.empty_done_workers()

    seconds += 1

print(seconds)
