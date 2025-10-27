import sys
import time

def ft_progress(lst):
	total = len(lst)
	start_time = time.time()

	for i, item in enumerate(lst):
		current = i + 1
		percent = (current / total) * 100
		elapsed_time = time.time() - start_time

		if current > 0:
			eta = (elapsed_time / current) * (total - current)
		else:
			eta = 0
		
		bar_len = 20
		filled_length = int(bar_len * current // total)
		bar = '█' * filled_length + '-' * (bar_len - filled_length)

		def format_time(seconds):
			mins, secs = divmod(int(seconds), 60)
			return f"{mins:02d}:{secs:02d}"

		progress = f"\rETA: {format_time(eta)} [{percent:3.2f}%] [{bar}] {current}/{total} | elapsed time {format_time(elapsed_time)}"
		sys.stdout.write(progress)
		sys.stdout.flush()
		yield item
	print()



listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)