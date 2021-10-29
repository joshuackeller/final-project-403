from django.http import HttpResponse

def indexPageView(request):
    output = '''
        <html>
            <head>
                <title>Index</title>
            </head>
            <body>
                <h1>Index Page View</h1>
            </body>
        </html>
    '''
    return(HttpResponse(output))

def menuPageView(request):
    return(HttpResponse('Menu page view'))

def editMenuPageView(request):
    return(HttpResponse('Edit menu page view'))
