import unittest
import os
import logging
from lesson_13.homework_13 import log_event, LOG_FILE

def read_last_line_from_log_file():
    with open(LOG_FILE, "r") as file:
        file_lines = file.readlines()
        last_line = file_lines[-1]
        return last_line

def get_added_user_log(username):
    with open(LOG_FILE, "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            if username in line:
                return line
        return None

class TestLogEvent(unittest.TestCase):

    def test_log_file_created(self):
        # print(BASE_DIR)
        # print(LOG_FILE)
        logging.shutdown()
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        log_event("Ronnie", "success")
        self.assertTrue(os.path.exists(LOG_FILE))

    def test_log_status_success(self):
        log_event("Neil", "success")
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                # added_user = read_last_line_from_log_file()
                added_user_1 = get_added_user_log("Neil")
                # print("success added_user", added_user)
                # print("success added_user_1", added_user_1)
            self.assertIn("Username: Neil", added_user_1)
            self.assertIn("Status: success", added_user_1)

    def test_log_status_expired(self):
        log_event("Judd", "expired")
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                # added_user = read_last_line_from_log_file()
                added_user_1 = get_added_user_log("Judd")
                # print("expired added_user", added_user)
                # print("expired added_user_1", added_user_1)
            self.assertIn("Username: Judd", added_user_1)
            self.assertIn("Status: expired", added_user_1)

    def test_log_status_failed(self):
        log_event("David", "failed")
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                # added_user = read_last_line_from_log_file()
                added_user_1 = get_added_user_log("David")
                # print("failed added_user", added_user)
                # print("failed added_user_1", added_user_1)
            self.assertIn("Username: David", added_user_1)
            self.assertIn("Status: failed", added_user_1)

    def test_log_status_unknown(self):
        log_event("Elliot", "blocked")
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                # added_user = read_last_line_from_log_file()
                added_user_1 = get_added_user_log("Elliot")
                # print("failed added_user", added_user)
                # print("failed added_user_1", added_user_1)
            self.assertIn("Username: Elliot", added_user_1)
            self.assertIn("Status: blocked", added_user_1)