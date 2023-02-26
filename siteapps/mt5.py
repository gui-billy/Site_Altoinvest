from datetime import datetime

from django.http import JsonResponse

CLIENTS = [
    {"broker": "GenialInvestimentos-PRD", "account": "461035", "exp_date": "2023-05-01"},
    {"broker": "XPMT5-PRD", "account": "75376", "exp_date": "2023-02-01"}
]


def mt5(request):
    if request.method == 'GET':
        data = request.GET.dict()
        if not data:
            response_data = {"ERRO": 'Dados inválidos'}
            return JsonResponse(response_data, status=400, json_dumps_params={'ensure_ascii': False})
        data_tuple = tuple(data.items())
        for item in CLIENTS:
            if (data_tuple[0][1] == item["broker"]) and (data_tuple[1][1] == item["account"]):
                dtt = datetime.strptime(item["exp_date"], "%Y-%m-%d")
                if (datetime.now() < dtt):
                    response_data = {"broker": data_tuple[0][1], "account": data_tuple[1][1], "exp_date": item["exp_date"]}
                    return JsonResponse(response_data, status=200, json_dumps_params={'ensure_ascii': False}) 
                else:
                    exp_date = datetime.strptime(item["exp_date"], "%Y-%m-%d").strftime("%d-%m-%Y")
                    response_data = {"ERRO": 'Licença Expirada', "Data": exp_date}
                    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
        response_data = {"ERRO": 'Conta Inválida'}
        return JsonResponse(response_data, status=200, json_dumps_params={'ensure_ascii': False})
    
    response_data = {"ERRO": 'Método Inválido'}
    return JsonResponse(response_data, status=400, json_dumps_params={'ensure_ascii': False})
                    
        
    

 