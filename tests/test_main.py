
from io import StringIO  # Python 3
import sys

import pytest

from hello_world.main import main

def test_main():

    # Create the in-memory "file"
    temp_out = StringIO()

    # Replace default stdout (terminal) with our stream
    sys.stdout = temp_out

    main()

    assert 'Hello world!\n' == temp_out.getvalue()

    # The original `sys.stdout` is kept in a special
    # dunder named `sys.__stdout__`. So you can restore
    # the original output stream to the terminal.
    sys.stdout = sys.__stdout__