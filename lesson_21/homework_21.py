from datetime import datetime

def process_log(inp_file, out_file, target_key):
    filtered_log = []


    with open(inp_file, 'r') as file:
        for line in file:
            if target_key in line:
                filtered_log.append(line)



    time_format = "%H:%M:%S"
    timestamps = []


    for log in filtered_log:
        timestamp_index = log.find("Timestamp ")
        if timestamp_index != -1:
            time_str = log[timestamp_index + len("Timestamp "):timestamp_index + len("Timestamp ") + 8]
            timestamps.append(datetime.strptime(time_str, time_format))


    with open(out_file, 'w') as logfile:
        for i in range(1, len(timestamps)):
            diff = (timestamps[i] - timestamps[i - 1]).total_seconds()
            if 31 < diff < 33:
                logfile.write(f"WARNING: Heartbeat delay {diff} seconds at {timestamps[i].strftime(time_format)}\n")
            elif diff >= 33:
                logfile.write(f"ERROR: Heartbeat delay {diff} seconds at {timestamps[i].strftime(time_format)}\n")


process_log("hblog.txt", "hb_test.log", "Key TSTFEED0300|7E3E|0400")