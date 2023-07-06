import heapq

a = [1, 2, 3, 4, 5, 6, 8, 0]
# heapify tao ra 1 headpq tu mang do
heap = list(a)  # max hit thi nhan voi -1
heapq.heapify(heap)
heapq.heappop(heap)
heapq.heappush(heap, -1)
print(heap)
print(heapq.nsmallest(3, a))
print(heapq.nlargest(3, a))
students = [
    {"name": "Qd", "gpa": 3.2},
    {"name": "Qd2", "gpa": 3.4},
    {"name": "Qd3", "gpa": 3.6},
    {"name": "Qd4", "gpa": 3.7},
]
print(heapq.nlargest(2, students, key=lambda x: x["gpa"]))
