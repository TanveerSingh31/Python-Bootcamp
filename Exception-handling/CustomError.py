class CustomError(Exception):
    def __init__(self, message, statusCode):
        super().__init__(message)
        self.statusCode = statusCode
    

def getData():
    try:
        raise CustomError("Data not present", 404)
    except Exception as e:
        print(e, e.statusCode)

getData()