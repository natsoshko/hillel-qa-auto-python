"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "login_system.log")

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.
    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу:
    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    # logging.basicConfig(
    #     filename='login_system.log',
    #     level=logging.INFO,
    #     format='%(asctime)s - %(message)s'
    #     )

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(message)s - %(levelname)s',
        force=True
    )

    logger = logging.getLogger("log_event")
    logger.setLevel(logging.DEBUG)

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


# log_event("Mark", status="success")
# log_event("Judd", status="expired")
# log_event("John", status="failed")


# if __name__ == "__main__":
#     log_event("Natalia", "success")
#     log_event("Ivan", "expired")
#     log_event("Petro", "failed")

