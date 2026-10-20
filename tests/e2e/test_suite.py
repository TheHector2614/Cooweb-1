#!/usr/bin/env python3
"""
Python Test Suite Wrapper for UltraRacha CRM E2E Tests
Delegates execution to tests/e2e/runner.js, ensuring seamless CLI compatibility
with 'python tests/e2e/test_suite.py' as documented in TEST_INFRA.md.
"""

import sys
import subprocess
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
    runner_path = os.path.join(script_dir, 'runner.js')

    print(f"[Python Test Suite Wrapper] Executing node {runner_path}...")
    sys.stdout.flush()

    cmd = ['node', runner_path] + sys.argv[1:]
    res = subprocess.run(cmd, cwd=project_root)
    sys.exit(res.returncode)

if __name__ == '__main__':
    main()
