from django.http import HttpResponse
from django.shortcuts import render

def start(request):
    data = {"name": request.GET.get("name", "None")}
    response = render(request, "index.html", data)
    response.set_cookie("passuser", "1234", 600)
    return response

def hello(request, name, kilometers):
    return HttpResponse(f"hello world"
    f"<div>{kilometers} & {name} & {request.COOKIES["passuser"]}</div> ")

def docx(request):
    host = request.META["HTTP_HOST"]
    user_agent  = request.META["HTTP_USER_AGENT"]
    query_string = request.path
    addr = request.META["REMOTE_ADDR"]
    remote_host = request.META["REMOTE_HOST"]
    method = request.META["REQUEST_METHOD"]
    server_name = request.META["SERVER_NAME"]
    server_port = request.META["SERVER_PORT"]
    language = request.META["HTTP_ACCEPT_LANGUAGE"]
    accept = request.META["HTTP_ACCEPT"]
    encoding = request.META["HTTP_ACCEPT_ENCODING"]
    return HttpResponse(f"""
                        <h1>Your:</h1>
                        <p>Host: {host},</p>
                        <p>Browser: {user_agent},</p>
                        <p>Query String: {host + query_string},</p>
                        <p>Addr: {addr},</p>
                        <p>Remote host: {remote_host},</p>
                        <p>Method: {method},</p>
                        <p>Server: {server_name},</p>
                        <p>Server port: {server_port},</p>
                        <p>Language: {language},</p>
                        <p>Type accept: {accept},</p>
                        <p>Encoding: {encoding}</p>
    """)

def test(request):
    number = int(request.GET.get("number", 200))
    if 100 > number or number > 599:
        number = 100
    return HttpResponse(status=number)