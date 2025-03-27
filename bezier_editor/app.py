#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bezier Curve Editor with Streamlit

Interactive web application for manipulating and comparing multiple Bezier curves.

Features:
- Display multiple predefined curves simultaneously
- Fine adjustment of curve parameters with small steps
- Color selection for each curve
- JSON import/export functionality
- CSV data export for all visible curves
- Reorganized UI with improved tab structure

To run:
1. Install the package: pip install bezier-editor
2. Run: bezier-editor
   or: python -m bezier_editor.app
"""

import streamlit as st
from bezier_editor.core.presets import get_presets, ensure_float
from bezier_editor.ui.sidebar import render_sidebar, render_curve_visibility
from bezier_editor.ui.main_view import render_visualization

def initialize_session_state():
    """
    Initialize Streamlit session state variables.
    """
    if 'curves' not in st.session_state:
        st.session_state.curves = ensure_float(get_presets())
    
    if 'active_curve' not in st.session_state:
        st.session_state.active_curve = 'Curve 1'
    
    if 'show_controls' not in st.session_state:
        st.session_state.show_controls = True
    
    if 'show_grid' not in st.session_state:
        st.session_state.show_grid = True

def main():
    """
    Main application entry point.
    """
    st.set_page_config(page_title="Bezier Curve Editor", page_icon="📊", layout="wide")
    
    st.title("Bezier Curve Editor")
    st.markdown("Interactive application for working with multiple Bezier curves.")
    
    # Initialize session state
    initialize_session_state()
    
    # Render curve visibility section (above main columns)
    render_curve_visibility()
    
    # Main layout: two columns
    col1, col2 = st.columns([1, 2])
    
    # Left column: Controls
    with col1:
        render_sidebar()
    
    # Right column: Visualization
    with col2:
        render_visualization()

if __name__ == "__main__":
    main()
