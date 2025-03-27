#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import streamlit.web.cli as stcli
from pathlib import Path

def main():
    """
    Run the Bezier Editor Streamlit app.
    """
    # Get the path to the app.py file
    app_path = Path(__file__).parent / "app.py"
    
    # Use Streamlit's CLI to run the app
    sys.argv = ["streamlit", "run", str(app_path.absolute())]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()