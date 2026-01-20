from urllib.parse import parse_qs
from db.connection import update_vlog
from utils.response import redirect


def update_post(body):
    data = parse_qs(body)

    vlog_id = data.get("id", [""])[0]
    title = data.get("title", [""])[0]
    content = data.get("content", [""])[0]

    if vlog_id.isdigit():
        update_vlog(int(vlog_id), title, content)

    return redirect("/")
