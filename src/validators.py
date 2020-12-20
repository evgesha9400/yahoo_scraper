

class ValidationError(Exception):
    """Invalid Request exception"""


def validate_input(req: str):
    """
    Validates user input
    :param req: user input
    :return: base, quote list
    """
    if ':' not in req:
        raise ValidationError("Input must contain colon character")
    from_ccy, to_ccy = req.split(":")
    to_ccy = to_ccy.strip("\n")
    if len(from_ccy) != 3 or len(to_ccy) != 3:
        raise ValidationError("Currency symbol must have a length of 3")
    return from_ccy, to_ccy
