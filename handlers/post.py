from urllib.parse import parse_qs

from db.connection import get_vlogs, add_vlog
from utils.response import response


def post_list():
    vlogs = get_vlogs()
    vlog_html = ""
    for title, desc, time in vlogs:
        vlog_html += f"""
        <div style="border:1px solid #ccc;padding:10px;margin:10px 0">
            <h2>{title}</h2>
            <p>{desc}</p>
            <small>{time}</small>
        </div>
        """

    body = f"""
    <html>
      <head>
        <title>Socket Vlogs</title>
      </head>
      <body>
        <h1>🎥 My Vlogs</h1>

        <form method="POST">
          <input name="title" placeholder="Vlog title" required><br><br>
          <textarea name="description" placeholder="Vlog description" required></textarea><br><br>
          <button type="submit">➕ Add Vlog</button>
        </form>

        <hr>
        {vlog_html}
      </body>
    </html>
    """

    return response(body)


def create_post(body):
    data = parse_qs(body)
    title = data.get("title", [""])[0]
    description = data.get("description", [""])[0]

    if title and description:
        add_vlog(title, description)

    return post_list()
