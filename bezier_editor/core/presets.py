#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Preset configurations for bezier curves.

This module provides predefined curve configurations that can be used
as starting points for curve editing.
"""

import numpy as np

def get_presets():
    """
    Get predefined curve configurations.
    
    Returns:
        dict: Preset configuration dictionaries
    """
    return {
        'Curve 1': {
            "x0": 0.0, "x1": 5.0, "x2": 10.0, "max_y": 6.0,
            "control_config": {
                "start_factor": 0.4, "start_height": 0.2,
                "peak_in_factor": 0.3, "peak_in_height": 0.9,
                "peak_out_factor": 0.3, "peak_out_height": 0.9,
                "end_factor": 0.4, "end_height": 0.2
            },
            "color": "#648FFF",  # Blue
            "visible": True
        },
        'Curve 2': {
            "x0": 0.0, "x1": 5.0, "x2": 10.0, "max_y": 6.0,
            "control_config": {
                "start_factor": 0.2, "start_height": 0.6,
                "peak_in_factor": 0.1, "peak_in_height": 0.95,
                "peak_out_factor": 0.4, "peak_out_height": 0.8,
                "end_factor": 0.3, "end_height": 0.2
            },
            "color": "#785EF0",  # Purple
            "visible": True
        },
        'Curve 3': {
            "x0": 0.0, "x1": 5.0, "x2": 10.0, "max_y": 6.0,
            "control_config": {
                "start_factor": 0.3, "start_height": 0.2,
                "peak_in_factor": 0.4, "peak_in_height": 0.8,
                "peak_out_factor": 0.1, "peak_out_height": 0.95,
                "end_factor": 0.2, "end_height": 0.6
            },
            "color": "#DC267F",  # Pink
            "visible": True
        },
        'Curve 4': {
            "x0": 0.0, "x1": 5.0, "x2": 10.0, "max_y": 6.0,
            "control_config": {
                "start_factor": 0.5, "start_height": 0.4,
                "peak_in_factor": 0.2, "peak_in_height": 0.85,
                "peak_out_factor": 0.2, "peak_out_height": 0.85,
                "end_factor": 0.5, "end_height": 0.4
            },
            "color": "#FE6100",  # Orange
            "visible": True
        },
        'Curve 5': {
            "x0": 0.0, "x1": 5.0, "x2": 10.0, "max_y": 6.0,
            "control_config": {
                "start_factor": 0.5, "start_height": 0.4,
                "peak_in_factor": 0.2, "peak_in_height": 0.85,
                "peak_out_factor": 0.2, "peak_out_height": 0.85,
                "end_factor": 0.5, "end_height": 0.4
            },
            "color": "#FFB000",  # Yellow
            "visible": True
        }
    }

def ensure_float(config):
    """
    Ensure all numeric values in config are float type.
    
    Args:
        config (dict): Configuration dictionary
        
    Returns:
        dict: Configuration with all numeric values converted to float
    """
    if isinstance(config, dict):
        for key, value in config.items():
            if isinstance(value, dict):
                config[key] = ensure_float(value)
            elif isinstance(value, (int, float, np.number)):
                config[key] = float(value)
    return config
