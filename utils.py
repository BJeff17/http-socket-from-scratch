def response_parser(resp):
    body = resp.get("body", b"")
    is_bytes = isinstance(body, bytes)

    headers = f"HTTP/1.1 {resp.get('status', 200)} {resp.get('message', 'OK')}\r\n"
    headers += f"Content-Length: {len(body)}\r\n"
    headers += f"Content-Type: {resp.get('content-type', 'text/html')}"

    if not is_bytes:
        headers += "; charset=utf-8"
    
    headers += "\r\nConnection: close\r\n\r\n"

    return headers.encode("utf-8") + (body if is_bytes else body.encode("utf-8"))

def file_reader(path, read_type='r'):
    with open(path, read_type) as file:
        return file.read()


def format_endpoint_as_path(endpoint):
    return f".{endpoint}"