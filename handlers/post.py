from urllib.parse import parse_qs

from db.connection import get_vlogs, add_vlog
from utils.response import response


def post_list():
    vlogs = get_vlogs()
    vlog_html = ""
    for vlog_id, title, desc, time in vlogs:
        vlog_html += f"""
        <div class="vlog-card">
      <div class="vlog-header">
        <h2>{title}</h2>
      </div>

      <p class="vlog-desc">{desc}</p>

      <div class="vlog-footer">
        <span class="vlog-date">{time}</span>
        
        <a href="/post/{vlog_id}/"><i class="bi bi-info-circle">detail</i></a>

        
        <form method="POST" action="/delete">
          <input type="hidden" name="id" value="{vlog_id}">
          <button class="delete-btn" type="submit">❌ Delete</button>
        </form>
      </div>
    </div>

        """

    body = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Socket Vlogs</title>

  <style>
    * {{
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }}

    body {{
      background: #f3f4f6;
      margin: 0;
      padding: 30px;
    }}

    h1 {{
      text-align: center;
      margin-bottom: 30px;
    }}

    .container {{
      max-width: 800px;
      margin: auto;
    }}

    .add-form {{
      background: #fff;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.08);
      margin-bottom: 30px;
    }}

    .add-form input,
    .add-form textarea {{
      width: 100%;
      padding: 10px;
      margin-bottom: 12px;
      border-radius: 6px;
      border: 1px solid #ccc;
      font-size: 14px;
    }}

    .add-form button {{
      background: #2563eb;
      color: #fff;
      border: none;
      padding: 10px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 15px;
    }}

    .add-form button:hover {{
      background: #1e40af;
    }}

    .vlog-card {{
      background: #fff;
      border-radius: 14px;
      padding: 20px;
      margin-bottom: 20px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
      transition: transform 0.2s ease;
    }}

    .vlog-card:hover {{
      transform: translateY(-3px);
    }}

    .vlog-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .vlog-header h2 {{
      margin: 0;
      font-size: 22px;
    }}

    .vlog-desc {{
      margin: 12px 0;
      font-size: 16px;
      color: #444;
    }}

    .vlog-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .vlog-date {{
      font-size: 13px;
      color: #888;
    }}

    .delete-btn {{
      background: none;
      border: none;
      color: #dc2626;
      font-size: 14px;
      cursor: pointer;
    }}

    .delete-btn:hover {{
      text-decoration: underline;
    }}
  </style>
</head>

<body>
  <h1>🎥 My Vlogs</h1>

  <div class="container">

    <!-- Add Vlog Form -->
    <form class="add-form" method="POST" action="/">
      <input type="text" name="title" placeholder="Vlog title" required>
      <textarea name="description" placeholder="Vlog description" required></textarea>
      <button type="submit">➕ Add Vlog</button>
    </form>
      {vlog_html}
  </div>
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
