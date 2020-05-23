'''
    Tests for saving application data into a pickle
'''
import os
import pytest
from src import global_variables
from src.backup import backup_data, load_data


def test_new_backup():
    '''
    Creates a new backup
    '''
    backup_data()
    assert os.path.exists("slackr_data.p")

def test_loading_backup():
    '''
    Loading existing data overwrites current data
    '''
    load_data()                                 
    assert len(global_variables.global_users) == 0
    assert len(global_variables.global_channels) == 0
    assert len(global_variables.global_valid_tokens) == 0
    assert global_variables.global_num_messages == 0
    assert len(global_variables.global_standups)  == 0

