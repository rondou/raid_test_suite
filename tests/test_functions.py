from pathlib import Path

import pytest

def test_write_001(cache):
    p: Path = cache / 'test_write_001.txt'
    with p.open(mode='a') as f:
        f.write('test_write_001')
    print(cache)
    assert True

def test_write_002():
    assert True
