#Get number of videos
n = int(input("Enter number of videos you want to process: "))

#Input each video
videos = []
for i in range(n):
	vid = input(f"Enter VideoID for Video {i+1}: ")
	arrival = int(input(f"Enter arrival time for Video {i+1}: "))
	burst = int(input(f"Enter burst time for Video {i+1}: "))
	videos.append({
		"vid": vid,
		"arrival_time": arrival,
		"burst_time": burst,
		"completion_time": 0,
		"turnaround_time": 0,
		"waiting_time": 0,
		"completed": False
	})

#Sort videos by arrival time
videos.sort(key=lambda x: x["arrival_time"])

#Initialize variables
current_time = 0
completed_count = 0

#SJF Non-Preemptive Scheduling
while completed_count < n:
	#Get available and not yet completed videos
	available = [v for v in videos if v["arrival_time"] <= current_time and not v["completed"]]

	if available:
		#Select video with shortest burst time
		short_video = min(available, key=lambda x: x["burst_time"])

		#Compute timing details
		current_time += short_video["burst_time"]
		short_video["completion_time"] = current_time
		short_video["turnaround_time"] = short_video["completion_time"] - short_video["arrival_time"]
		short_video["waiting_time"] = short_video["turnaround_time"] - short_video["burst_time"]
		short_video["completed"] = True

		completed_count += 1
	else:
		current_time += 1	#If no video is available, increase time


#Print table
print("\n" + "-"*65)
print("VideoID | Arrival | Burst | Completion | Turnaround | Waiting")
print("-"*65)

#Sort back the videos
videos.sort(key=lambda x: x["vid"])

for v in videos:
    print(f"{v['vid']:>7} |"
          f"{v['arrival_time']:>8} |"
          f"{v['burst_time']:>6} |"
          f"{v['completion_time']:>11} |"
          f"{v['turnaround_time']:>11} |"
          f"{v['waiting_time']:>8}")

print("-"*65)

avg_tat = sum(v["turnaround_time"] for p in videos) / n
avg_wt = sum(v["waiting_time"] for p in videos) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")