from datetime import datetime
import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_LOG_FILE = os.path.join(BASE_DIR, "hblog.txt")
OUTPUT_LOG_FILE = os.path.join(BASE_DIR, "hb_test.log")
SEARCH_KEY = "Key TSTFEED0300|7E3E|0400"

def get_timestamp(line):
    start = line.find("Timestamp ") + len("Timestamp ")
    timestamp = line[start:start + 8]
    # print(start, timestamp)
    return datetime.strptime(timestamp, "%H:%M:%S")

def func_analyze_heartbeat_log():
    filtered_log = []

    if os.path.exists(OUTPUT_LOG_FILE):
        os.remove(OUTPUT_LOG_FILE)

    with open(INPUT_LOG_FILE, "r") as file:
        for line in file:
            if SEARCH_KEY in line:
                filtered_log.append(line)

    logging.basicConfig(
        filename=OUTPUT_LOG_FILE,
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s: %(message)s",
        force=True
    )

    for i in range(len(filtered_log) - 1):
        current = filtered_log[i]
        next_line = filtered_log[i + 1]

        current_time = get_timestamp(current)
        next_time = get_timestamp(next_line)

        heartbeat = (current_time - next_time).total_seconds()

        if 31 < heartbeat < 33:
            logging.warning(f"Heartbeat {heartbeat:.0f} sec at time {current_time.strftime('%H:%M:%S')}")
        elif heartbeat >= 33:
            logging.error(f"Heartbeat {heartbeat:.0f} sec at time {current_time.strftime('%H:%M:%S')}")

    logging.shutdown()

func_analyze_heartbeat_log()