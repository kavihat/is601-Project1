'''
Controller to render page4.html
'''
from flask import render_template
# don't change this import or it can't find the module controller
from .controller import ControllerBase


class Page4Controller(ControllerBase):
    '''
    To define about controller class  for get
    '''
    @staticmethod
    def get():
        '''
        To define static method for get
        '''
        name = "Kavitha Kannanunny"
        return render_template('page4.html', name=name)
