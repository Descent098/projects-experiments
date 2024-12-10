# Semaphore

A semaphore is a synchronization primative that allows you to let multiple threads enter the critical section. The semaphore implemented in `sem.py` is a counting semaphore with a condition variable associated, meaning you don't need to sleep between critical sections.

Compared to the traditional condition variable there are a few specifics to python:

1. You need to use `threading.Thread`
2. Since it works as a context manager you can use `with self.condition:` to make sure the lock is acquired and released as expected

## Resources 

- [What is a semaphore? How do they work? (Example in C)](https://www.youtube.com/watch?v=ukM_zzrIeXs)
- [Semaphore | Signaling, Telegraphy, Flags | Britannica](https://www.britannica.com/technology/semaphore)
- [Semaphores in Process Synchronization - GeeksforGeeks](https://www.geeksforgeeks.org/semaphores-in-process-synchronization/)
