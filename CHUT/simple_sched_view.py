from django.http import HttpResponse
import model.data as data


def simple_response(request):

    html = """ <!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>CHUT</title>
                    <link rel="stylesheet" href="styles.css">
                    </head>\n"""

    json_data = """ [{"station": "university", "line": "red", "hour": "11", "minute": "32", "second": "12"},
                     {"station": "university", "line": "red", "hour": "12", "minute": "32", "second": "12"}]"""

    schedule = data.schedule_from_json(json_data)

    html += '<body>'
    for item in schedule:
        html += f"<p> {str(item)} </p>\n"
    html += '</body>'

    return HttpResponse(html)


