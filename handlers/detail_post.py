from db.connection import find_vlogs
from handlers.not_found import not_found
from utils.response import response


def detail_post(vlog_id):
    vlog = find_vlogs(vlog_id)
    if not vlog:
        return not_found()

    vlog = vlog[0]

    vlog_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Post</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">

<form method="POST" action="/update">

    <input type="hidden" name="id" value="{vlog[0]}">

    <div class="mb-3">
        <label class="form-label">Title</label>
        <input
            type="text"
            class="form-control"
            name="title"
            value="{vlog[1]}"
            required>
    </div>

    <div class="mb-3">
        <label class="form-label">Content</label>
        <textarea
            class="form-control"
            name="content"
            rows="5"
            required>{vlog[2]}</textarea>
    </div>

    <button type="submit" class="btn btn-primary">
        Update
    </button>

    <a href="/" class="btn btn-secondary ms-2">Back</a>
</form>


</body>
</html>
"""
    return response(vlog_html)
