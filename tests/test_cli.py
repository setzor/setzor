import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from setzor.cli import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from setzor" in captured.out
