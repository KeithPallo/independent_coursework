# python3

import heapq

class prob_thread:
    def __init__(self,id,free_time = 0):
        self.id = id
        self.free_time = free_time


    def __lt__(self, other):
        if self.free_time == other.free_time:
            return self.id < other.id
        return self.free_time < other.free_time


    def __gt__(self, other):
        if self.free_time == other.free_time:
            return self.id > other.id
        return self.free_time > other.free_time


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.size = m
        self.result = []
        self.thread_queue = [prob_thread(i) for i in range (self.num_workers)]


    def write_response(self):

        for thread_id, start_time in self.result:
          print(thread_id,start_time)

    def assign_jobs(self):

        for job in self.jobs:

            thread = heapq.heappop(self.thread_queue)

            self.result.append((thread.id,thread.free_time))

            thread.free_time += job

            heapq.heappush(self.thread_queue,thread)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

