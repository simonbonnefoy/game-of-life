import time
def show_Remaining_Time(time_delta):
     print(' \r%d:Time Remaining' % time_delta, end = '',flush=False)

if __name__ == '__main__':
    count = 0
    while True and count < 10:
        show_Remaining_Time(count)
        count += 1
        time.sleep(1)
