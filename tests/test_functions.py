from pathlib import Path

import pytest
import hashlib
import shutil

def test_write_001(cache):
    p: Path = cache / 'test_write_001.txt'
    with p.open(mode='a') as f:
        f.write('test_write_001')

    c: str = ''
    with p.open(mode='r') as f:
        c = f.read()

    assert c == 'test_write_001'

def test_write_002(cache):
    p: Path = cache / 'test_write_002.txt'
    with p.open(mode='a') as f:
        f.write('test_write_002')

    to_file = cache / 'test_write_002.txt.bak'
    shutil.copy(p, to_file)

    m = hashlib.md5()
    m2 = hashlib.md5()
    o: str = ''
    t: str = ''
    with p.open(mode='rb') as f, to_file.open(mode='rb') as fs:
        for chunk in iter(lambda: f.read(4096), b''):
            m.update(chunk)
        for chunk in iter(lambda: fs.read(4096), b''):
            m2.update(chunk)

        o = m.hexdigest()
        t = m2.hexdigest()
    assert o == t
