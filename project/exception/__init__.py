import sys

class WheatKernalException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message= WheatKernalException.get_detailed_error_message(error_message=error_message,
                                                                            error_detail=error_detail)
        
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys):
        _,_,exec_tb = error_detail.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script:
        [{file_name}] at 
        try block line No: [{try_block_line_number}] & excepton block LineNo: [{exception_block_line_number}]
        error_message: [{error_message}]
        """
        return error_message
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return WheatKernalException.__name__.str()