import sys


def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in pythong script [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error = error
        self.error_detail = error_detail

    def __str__(self):
        return error_message_details(self.error,self.error_detail)
    

