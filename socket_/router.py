from handlers.detail_post import detail_post
from handlers.not_found import not_found
from handlers.post import post_list, create_post
from handlers.delete_post import delete_post


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
    if path == "/delete" and method == "POST":
        return delete_post(body)
    if method == 'GET' and path.startswith('/post'):
        vlog_id = path.split('/')[2]
        if vlog_id.isdigit():
            return detail_post(vlog_id)
    return not_found()
