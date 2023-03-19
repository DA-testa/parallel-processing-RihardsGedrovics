def parallel_processing(num_threads, num_jobs, job_times):
    output = []
    next_free_time = [0] * num_threads
    threads = list(range(num_threads))
    for job_index, job_time in enumerate(job_times):
        next_thread = min(threads, key=lambda i: next_free_time[i])
        output.append((next_thread, next_free_time[next_thread]))
        next_free_time[next_thread] += job_time
    return output

def main():
    num_threads, num_jobs = map(int, input().split())
    job_times = list(map(int, input().split()))
    result = parallel_processing(num_threads, num_jobs, job_times)
    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
