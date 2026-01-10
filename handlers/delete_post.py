from urllib.parse import parse_qs

from db.connection import delete_vlog
from utils.response import response
from handlers.post import post_list


def delete_post(body):
    data = parse_qs(body)
    vlog_id = data.get("id", [""])[0]

    if vlog_id.isdigit():
        delete_vlog(int(vlog_id))

    return post_list()


def redirect(path):
    return (
        "HTTP/1.1 303 See Other\r\n"
        f"Location: {path}\r\n"
        "\r\n"
    )
