import pytest

from . import workouts
from .workouts import print_workout_days


@pytest.mark.parametrize('test_input, expected', [
    ('body', 'Mon, Tue, Thu, Fri\n'),
    ('BODY', 'Mon, Tue, Thu, Fri\n'),
    ('legs', 'No matching workout\n'),
    ('#1', 'Mon, Tue\n')
])
def test_print_workout_days(test_input: str, expected: str, capsys):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert expected == captured.out


def test_print_workout_days_with_custom_workouts(capsys):
    print_workout_days('legs', {'_moN': 'legs'})
    captured = capsys.readouterr()
    assert '_Mon\n' == captured.out

    print_workout_days('arms', {'_moN': 'legs'})
    captured = capsys.readouterr()
    assert 'No matching workout\n' == captured.out

    print_workout_days('arms', {'': 'legs'})
    captured = capsys.readouterr()
    assert 'No matching workout\n' == captured.out


def test_workout_glob():
    for k, v in workouts.WORKOUTS.items():
        assert v in ['upper body #1', 'lower body #1',
                     '30 min cardio', 'upper body #2',
                     'lower body #2']
        assert k in ['mon', 'tue', 'wed', 'thu', 'fri']
