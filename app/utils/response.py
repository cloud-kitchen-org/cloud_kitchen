def standard_response(data=None, message="Success", status=200):
    return {
        "status": status,
        "message": message,
        "data": data,
    }
