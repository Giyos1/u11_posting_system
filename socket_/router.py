from handlers.not_found import not_found
from handlers.post import post_list, create_post


def handle_request(raw_request: bytes) -> bytes:
    try:
        text = raw_request.decode("utf-8", errors="ignore")
        line = text.split("\r\n", 1)[0]
        _, _, body = text.partition("\r\n\r\n")

        method, path, _ = line.split(" ")
    except Exception:
        return not_found()

    if method == "GET" and path == "/":
        return post_list()
    if method == "POST" and path == "/":
        return create_post(body)
    return not_found()
