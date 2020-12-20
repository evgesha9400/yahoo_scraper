import socket
import time
import logging
from scraper import get_rate, CcyPairNotFound
from validators import validate_input, ValidationError
from settings import ServerEnv

ENV = ServerEnv()
logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(ENV.log_level)


def send_string(conn, string: str):
    conn.sendall((string + "\n").encode())


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((ENV.host, ENV.port))
            s.listen()
            LOGGER.info(f"Server started {ENV.host}:{ENV.port}")
            conn, addr = s.accept()
            with conn:
                LOGGER.info(f"Connected by {addr}")
                send_string(conn, "Connected!")
                while True:

                    req = conn.recv(4096).decode()

                    try:
                        from_ccy, to_ccy = validate_input(req)
                        start_time = time.process_time()
                        rate = get_rate(from_ccy, to_ccy)
                        LOGGER.info(
                            f"Elapsed time: {time.process_time() - start_time} seconds"
                        )
                        send_string(conn, rate)
                    except CcyPairNotFound:
                        LOGGER.warning(f"{from_ccy}/{to_ccy} currency pair not found")
                        send_string(conn, f"Currency pair not found. Try again")
                    except ValidationError as e:
                        LOGGER.warning(f"Bad request: {e}")
                        send_string(conn, f"Bad request: {e}")

        finally:
            LOGGER.info("Closing socket")
            s.close()


if __name__ == "__main__":
    main()
