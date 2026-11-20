def convert_date_format(date_str):
    """
    Converts a date string from 'YYYY-MM-DD' format to 'DD/MM/YYYY' format.
    
    Parameters:
    date_str (str): The date string in 'YYYY-MM-DD' format.
    
    Returns:
    str: The date string in 'DD/MM/YYYY' format.
    """
    year, month, day = date_str.split('-')
    return f"{day}/{month}/{year}"
