from django.http import HttpResponse, JsonResponse
from .utils import clean_number_list

import json


def index_home(request):
    """
    / location
    """
    return HttpResponse(status=404)


def total(request):
    """
    Input: POST "numbers_to_add"
    Output: JSONResponse with the sum of the list or Error
    """
    if request.method == 'POST':
        # Extract the list of numbers from the POST
        try:
            json_body = json.loads(request.body)
        except Exception as e:
            # print(type(e))
            # TODO # Print to log file
            return JsonResponse({"status": "error",
                                "msg": "\"numbers_to_add\" is invalid"},
                                safe=False, status=400)

        # Validate that the numbers_to_add is in the json payload
        if "numbers_to_add" not in json_body:
            return JsonResponse({"status": "error",
                                "msg": "Missing \"numbers_to_add\" field"},
                                safe=False, status=400)

        numbers_to_add = json_body["numbers_to_add"]

        # If numbers_to_add is empty, return 0
        if numbers_to_add == '' or numbers_to_add == '[]':
            return JsonResponse({"total": str(0)}, safe=False, status=200)

        # Validate that the numbers_to_add field is evaluated to be a list
        if isinstance(numbers_to_add, list) is False:
            return JsonResponse({"status": "error",
                    "msg": "\"numbers_to_add\" must be a list object"},
                    safe=False, status=400)

        # Clean the numbers_to_add list, and return error if necessary
        numbers_to_add_list = clean_number_list(numbers_to_add)
        if numbers_to_add_list is False:
            return JsonResponse({"status": "error",
                    "msg": "\"numbers_to_add\" contains invalid values"},
                    safe=False, status=400)

        # Sum the list of numbers together
        sum_of_numbers = sum(numbers_to_add_list)

        # Return the total
        return JsonResponse({"total": str(sum_of_numbers)},
                            safe=False, status=200)

    else:
        return HttpResponse(status=405)
