import pytest
import shutil

from pathlib import Path


@pytest.fixture(scope='function')
def cache(request):
    p = Path(".") / '.cache'
    p.mkdir(parents=True, exist_ok=False)
    yield p
    shutil.rmtree(str(p))
