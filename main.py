#!/usr/bin/env python3
"""
diagram-maker: 1-Click Execution & Entrypoint
Run without arguments to compile all specs, or provide a specific spec file path.
"""

import sys
from src.cli import main

if __name__ == "__main__":
    sys.exit(main())
