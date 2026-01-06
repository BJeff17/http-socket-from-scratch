from utils import file_reader, response_parser, format_endpoint_as_path


def index_view(req):

    resp = {
    "body": file_reader("./views/index.html"),
    "status":200
}

    return  response_parser(resp)


def _404_view(req):
    resp = {
    "body":file_reader("./views/404.html"),
    "status":404
}
    return  response_parser(resp)



def file_view(req, content_type="text/css"):

    try :
        return response_parser({
            "body": file_reader(format_endpoint_as_path(req["endpoint"]), 'rb'),
            "content-type": content_type,
            "status": 200
        })
    except:
        return _404_view(req)