from students import StudentDB
import pytest


@pytest.fixture(scope='module')
def db():
    print('--------setup------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('--------teardown------------')
    db.close()

def test_student_bodzio(db):
    student = db.get_data('Bodzio')
    assert student['id'] == 1
    assert student['name'] == 'Bodzio'
    assert student['result'] == 'pass'

def test_student_krupek(db):
    student = db.get_data('Krupek')
    assert student['id'] == 2
    assert student['name'] == 'Krupek'
    assert student['result'] == 'fail'