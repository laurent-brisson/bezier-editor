#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UI components for the main visualization area.

This module contains Streamlit UI components for the main visualization area,
including the bezier curve plot and curve data export functionality.
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bezier_editor.core.bezier import create_simple_bezier_curve, generate_controlled_curve
from bezier_editor.core.presets import ensure_float
from bezier_editor.io.file_operations import prepare_curves_for_csv_export

def render_visualization():
    """
    Render the main visualization area with curve plots and data export.
    """
    st.header("Visualization")
    
    try:
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Collect all curve data for CSV export
        all_curve_data = {}
        
        # Plot visible curves
        for curve_name, curve_config in st.session_state.curves.items():
            if curve_config.get("visible", True):
                # Calculate key points and control points from current config
                key_points, control_points = create_simple_bezier_curve(
                    float(curve_config["x0"]), 
                    float(curve_config["x1"]), 
                    float(curve_config["x2"]), 
                    float(curve_config["max_y"]), 
                    ensure_float(curve_config["control_config"])
                )
                
                # Generate the curve
                x_curve, y_curve = generate_controlled_curve(key_points, control_points)
                
                # Plot the curve
                ax.plot(x_curve, y_curve, color=curve_config["color"], linewidth=3, 
                       label=curve_name)
                
                # Store curve data for CSV export
                all_curve_data[curve_name] = {
                    'x': x_curve,
                    'y': y_curve
                }
                
                # Plot the key points
                ax.scatter([p[0] for p in key_points], [p[1] for p in key_points], 
                          color=curve_config["color"], s=80, edgecolor='black', alpha=0.8, zorder=10)
                
                # Plot control points if enabled
                if st.session_state.show_controls:
                    # Plot the control points
                    cp_x = [p[0] for p in control_points]
                    cp_y = [p[1] for p in control_points]
                    ax.scatter(cp_x, cp_y, color=curve_config["color"], marker='x', s=60, alpha=0.7, zorder=5)
                    
                    # Plot the control handles
                    for i, (kp, cp) in enumerate(zip([key_points[0], key_points[1], key_points[1], key_points[2]], 
                                                   control_points)):
                        ax.plot([kp[0], cp[0]], [kp[1], cp[1]], '--', color=curve_config["color"], alpha=0.5, linewidth=1)
        
        # Configure the plot
        x_values = []
        y_values = []
        
        for curve_name, curve_config in st.session_state.curves.items():
            if curve_config.get("visible", True):
                x_values.extend([curve_config["x0"], curve_config["x1"], curve_config["x2"]])
                y_values.extend([0, curve_config["max_y"], 0])
        
        if x_values and y_values:
            ax.set_xlim(min(x_values) - 1, max(x_values) + 1)
            ax.set_ylim(-0.5, max(y_values) * 1.2)
        
        ax.set_title('Bezier Curves Comparison', fontsize=14, fontweight='bold')
        ax.set_xlabel('X', fontsize=12)
        ax.set_ylabel('Y', fontsize=12)
        ax.legend()
        
        if st.session_state.show_grid:
            ax.grid(True, alpha=0.3)
        
        # Display the plot
        st.pyplot(fig)
        
        # Export curve data
        if all_curve_data:
            with st.expander("Curve Data"):
                # Prepare data for CSV export
                curve_df = prepare_curves_for_csv_export(all_curve_data)
                
                # Display a sample of the data
                sample_size = min(100, len(curve_df))
                st.dataframe(curve_df.head(sample_size))
                
                # Download button for full data
                csv_string = curve_df.to_csv(index=False)
                st.download_button(
                    label="Download All Curve Data (CSV)",
                    data=csv_string,
                    file_name="all_bezier_curves.csv",
                    mime='text/csv',
                )
    
    except Exception as e:
        st.error(f"Error generating curves: {str(e)}")
        st.error("Try adjusting parameters to obtain valid curves.")
