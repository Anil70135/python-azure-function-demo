import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if not name:
        return func.HttpResponse("Hello, Team! This is our live demo function.", status_code=200)
    return func.HttpResponse(f"Hello, {name}! Welcome to the Azure Function demo.", status_code=200)
