'''
This file provides shared pytests and fixtures for all System Tests
'''
import pytest
from src.global_variables import workspace_reset

@pytest.fixture(autouse=True, scope='function')
def clean_application():
    '''
    Deletes all application data
    '''
    workspace_reset()
