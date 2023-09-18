
def convert_percent_string_to_float(percent_string: str):
    return float(percent_string.replace('%', ''))/100


def bulk_convert_percent_string_to_float(stock_info_dict: dict, percent_string_list: list):
    for percent_string in percent_string_list:
        stock_info_dict[percent_string] = convert_percent_string_to_float(stock_info_dict[percent_string])
    return stock_info_dict