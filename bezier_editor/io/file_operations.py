#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File operations for bezier curve configurations.

This module handles importing and exporting curve configurations in JSON format,
as well as exporting curve data points to CSV.
"""

import json
import copy
import pandas as pd
import numpy as np
import streamlit as st
from bezier_editor.core.presets import ensure_float

def export_curves_json():
    """
    Export all curves as a JSON string.
    
    Returns:
        str: JSON string of all curves
    """
    export_data = copy.deepcopy(st.session_state.curves)
    return json.dumps(export_data, indent=4)

def import_curves_json(json_str):
    """
    Import curves from a JSON string.
    
    Args:
        json_str (str): JSON string containing curve configurations
        
    Returns:
        bool: Success status
    """
    try:
        imported_data = json.loads(json_str)
        # Validate imported data structure
        for curve_name, curve_data in imported_data.items():
            if not isinstance(curve_data, dict):
                return False
            required_keys = ["x0", "x1", "x2", "max_y", "control_config", "color"]
            if not all(key in curve_data for key in required_keys):
                return False
            if not isinstance(curve_data["control_config"], dict):
                return False
            control_keys = ["start_factor", "start_height", "peak_in_factor", "peak_in_height", 
                           "peak_out_factor", "peak_out_height", "end_factor", "end_height"]
            if not all(key in curve_data["control_config"] for key in control_keys):
                return False
        
        # All validation passed, update session state
        st.session_state.curves = ensure_float(imported_data)
        return True
    except Exception as e:
        st.error(f"Error importing JSON: {str(e)}")
        return False

def prepare_curves_for_csv_export(all_curve_data):
    """
    Prepare curve data for CSV export.
    
    Args:
        all_curve_data (dict): Dictionary containing curve data points
        
    Returns:
        pandas.DataFrame: DataFrame ready for CSV export
    """
    if not all_curve_data:
        return pd.DataFrame()
        
    # Find the maximum length of any curve
    max_length = 0
    for curve_name, data in all_curve_data.items():
        max_length = max(max_length, len(data['x']))
    
    # Create a DataFrame with columns for each curve
    csv_data = {}
    for curve_name, data in all_curve_data.items():
        # Pad shorter curves with NaN
        x_padded = np.pad(data['x'], (0, max_length - len(data['x'])), 
                         'constant', constant_values=np.nan)
        y_padded = np.pad(data['y'], (0, max_length - len(data['y'])), 
                         'constant', constant_values=np.nan)
        
        csv_data[f"{curve_name}_x"] = x_padded
        csv_data[f"{curve_name}_y"] = y_padded
    
    return pd.DataFrame(csv_data)
