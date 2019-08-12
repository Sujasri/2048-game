def buildErrorString(diagnostic=None):
    """
        returns a dictionary containing the specified key and accompanying diagnostic information
        :param
            diagnostic:     A string that describes the error
        :return:    A dictionary that contains the specified error key having a value that
                    consists of the specfied error string followed by a free-form diagnostic message
    """
    ERROR_PROPERTY = u'gameStatus'
    ERROR_PREFIX = u'error:  '
    return {ERROR_PROPERTY: ERROR_PREFIX + diagnostic}