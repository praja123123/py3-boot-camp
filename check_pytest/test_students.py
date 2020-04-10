from students import StudentDB
import pytest

db = None

def setup_module(module):
    print('--------setup------------')
    global db
    db = StudentDB()
    db.connect('data.json')

def teardown_module(module):
    print('--------teardown------------')
    db.close()

def test_student_bodzio():
    student = db.get_data('Bodzio')
    assert student['id'] == 1
    assert student['name'] == 'Bodzio'
    assert student['result'] == 'pass'

def test_student_krupek():
    student = db.get_data('Krupek')
    assert student['id'] == 2
    assert student['name'] == 'Krupek'
    assert student['result'] == 'fail'