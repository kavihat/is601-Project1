"""
Adding context processors
"""
from os import getenv
import datetime


def utility_text_processors():
    """
    Adding utility text processors
    """
    message = "hello world"

    def deployment_environment():
        """Setting deployment environment"""
        return getenv('FLASK_ENV', None)

    def current_year():
        """Setting current year format"""
        current_date_time = datetime.datetime.now()
        date = current_date_time.date()
        year = date.strftime("%Y")
        return year
    '''
    def format_price(amount, currency="$"):
        """Setting currency format"""
        return f"{currency}{amount:.2f}"
    '''
    return dict(
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year()
    )
