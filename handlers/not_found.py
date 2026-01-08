from utils.response import response


def not_found():
    with open('template/not_found.html') as f:
        body = f.read()
    return response(body)
