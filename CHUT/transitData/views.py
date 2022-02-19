from django.http import HttpResponse

def index(request):
    return HttpResponse("""<table><tr><th>Station</th>
        <th>Line</th>
        <th>Time</th>
    </tr>
    <tr>
        <td>example station</td>
        <td>example line</td>
        <td>example time</td>
    </tr>
</table>""")

