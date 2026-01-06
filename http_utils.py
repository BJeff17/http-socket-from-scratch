from views import _404_view, file_view, index_view

mimes = {
    # Text
    ".html": "text/html",
    ".htm": "text/html",
    ".css": "text/css",
    ".txt": "text/plain",
    ".csv": "text/csv",
    ".xml": "application/xml",
    ".json": "application/json",

    # JavaScript
    ".js": "application/javascript",
    ".mjs": "application/javascript",

    # Images
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".webp": "image/webp",
    ".bmp": "image/bmp",
    ".tiff": "image/tiff",

    # Fonts
    ".woff": "font/woff",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".otf": "font/otf",

    # Audio
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
    ".ogg": "audio/ogg",

    # Video
    ".mp4": "video/mp4",
    ".webm": "video/webm",
    ".ogv": "video/ogg",

    # Archives
    ".zip": "application/zip",
    ".tar": "application/x-tar",
    ".gz": "application/gzip",
    ".rar": "application/vnd.rar",
    ".7z": "application/x-7z-compressed",

    # PDF & docs
    ".pdf": "application/pdf",
    ".doc": "application/msword",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".xls": "application/vnd.ms-excel",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    # WASM
    ".wasm": "application/wasm",
}



def http_request_parser(http_response:bytes):
    rep = http_response.decode('utf-8').split()
    return {
        "method": rep[0],
        "endpoint": rep[1],

    }




def http_response(out):
    out = http_request_parser(out)

    match(out["endpoint"]):
        case '/':
            return index_view(out)
    for k, v in mimes.items():
        if out["endpoint"].endswith(k):
            return file_view(out, v)

    return _404_view(out)