#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner
from django.core.management import execute_from_command_line


if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'bio.tests.settings'
    django.setup()

    if sys.argv[1:]:
        execute_from_command_line(sys.argv)
        sys.exit(0)

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["bio.tests"])
    sys.exit(bool(failures))
