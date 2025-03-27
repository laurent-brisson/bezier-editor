#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UI components for the control panel (sidebar).

This module contains Streamlit UI components for the control sidebar,
including key point editors, control point editors, and appearance settings.
"""

import streamlit as st
from bezier_editor.io.file_operations import export_curves_json, import_curves_json

def render_key_points_tab(active_curve):
    """
    Render the key points editing tab.
    
    Args:
        active_curve (str): Name of the currently selected curve
    """
    st.subheader("Key Points")
    
    # Ensure values are float
    curve_config = st.session_state.curves[active_curve]
    
    # Combine slider and number input for fast and precise control
    col_slider, col_input = st.columns([3, 1])
    
    with col_slider:
        x0_slider = st.slider(
            "Start point (x0)", 
            min_value=-10.0, max_value=30.0, 
            value=float(curve_config["x0"]), 
            step=0.1,
            key=f"x0_slider_{active_curve}"
        )
    
    with col_input:
        x0_input = st.number_input(
            "", 
            min_value=-10.0, max_value=30.0, 
            value=x0_slider, 
            step=0.01,
            format="%.2f",
            key=f"x0_input_{active_curve}"
        )
    
    # Update session state with either slider or input value (input takes precedence)
    st.session_state.curves[active_curve]["x0"] = x0_input
    
    # Peak position with slider and number input
    col_slider, col_input = st.columns([3, 1])
    
    with col_slider:
        x1_slider = st.slider(
            "Peak position (x1)", 
            min_value=-10.0, max_value=30.0, 
            value=float(curve_config["x1"]), 
            step=0.1,
            key=f"x1_slider_{active_curve}"
        )
    
    with col_input:
        x1_input = st.number_input(
            "", 
            min_value=-10.0, max_value=30.0, 
            value=x1_slider, 
            step=0.01,
            format="%.2f",
            key=f"x1_input_{active_curve}"
        )
    
    st.session_state.curves[active_curve]["x1"] = x1_input
    
    # Peak height with slider and number input
    col_slider, col_input = st.columns([3, 1])
    
    with col_slider:
        max_y_slider = st.slider(
            "Peak height (max_y)", 
            min_value=0.1, max_value=30.0, 
            value=float(curve_config["max_y"]), 
            step=0.1,
            key=f"max_y_slider_{active_curve}"
        )
    
    with col_input:
        max_y_input = st.number_input(
            "", 
            min_value=0.1, max_value=30.0, 
            value=max_y_slider, 
            step=0.01,
            format="%.2f",
            key=f"max_y_input_{active_curve}"
        )
    
    st.session_state.curves[active_curve]["max_y"] = max_y_input
    
    # End point with slider and number input
    col_slider, col_input = st.columns([3, 1])
    
    with col_slider:
        x2_slider = st.slider(
            "End point (x2)", 
            min_value=-10.0, max_value=30.0, 
            value=float(curve_config["x2"]), 
            step=0.1,
            key=f"x2_slider_{active_curve}"
        )
    
    with col_input:
        x2_input = st.number_input(
            "", 
            min_value=-10.0, max_value=30.0, 
            value=x2_slider, 
            step=0.01,
            format="%.2f",
            key=f"x2_input_{active_curve}"
        )
    
    st.session_state.curves[active_curve]["x2"] = x2_input

def render_control_point_editor(active_curve, cp_name, cp_title, factor_key, height_key, reference_point):
    """
    Render editor for a single control point.
    
    Args:
        active_curve (str): Name of the currently selected curve
        cp_name (str): Identifier for the control point
        cp_title (str): Display title for the control point
        factor_key (str): Key for the horizontal factor in control_config
        height_key (str): Key for the vertical factor in control_config
        reference_point (str): Description of the reference point
    """
    st.subheader(cp_title)
    
    ctrl_config = st.session_state.curves[active_curve]["control_config"]
    
    # Horizontal factor with slider and number input
    col_slider, col_input = st.columns([3, 1])
    
    with col_slider:
        factor_slider = st.slider(
            "Horizontal factor", 
            min_value=0.01, max_value=1.0,
            value=float(ctrl_config[factor_key]), 
            step=0.05,
            key=f"{cp_name}_factor_slider_{active_curve}"
        )
    
    with col_input:
        factor_input = st.number_input(
            "", 
            min_value=0.01, max_value=1.0,
            value=factor_slider, 
            step=0.01,
            format="%.2f",
            key=f"{cp_name}_factor_input_{active_curve}"
        )
    
    st.session_state.curves[active_curve]["control_config"][factor_key] = factor_input
    
    # Relative height with slider and number input
    col_slider, col_input = st.columns([3, 1])
    
    with col_slider:
        height_slider = st.slider(
            "Relative height", 
            min_value=0.0, max_value=1.0,
            value=float(ctrl_config[height_key]), 
            step=0.05,
            key=f"{cp_name}_height_slider_{active_curve}"
        )
    
    with col_input:
        height_input = st.number_input(
            "", 
            min_value=0.0, max_value=1.0,
            value=height_slider, 
            step=0.01,
            format="%.2f",
            key=f"{cp_name}_height_input_{active_curve}"
        )
    
    st.session_state.curves[active_curve]["control_config"][height_key] = height_input
    
    # Visual explanation
    st.markdown("---")
    st.info(reference_point)

def render_appearance_tab(active_curve):
    """
    Render the appearance settings tab.
    
    Args:
        active_curve (str): Name of the currently selected curve
    """
    st.subheader("Appearance")
    
    # Color picker
    st.session_state.curves[active_curve]["color"] = st.color_picker(
        "Curve color", 
        value=st.session_state.curves[active_curve]["color"],
        key=f"color_{active_curve}"
    )
    
    # Display options
    st.session_state.show_controls = st.checkbox(
        "Show control points", 
        value=st.session_state.show_controls
    )
    
    st.session_state.show_grid = st.checkbox(
        "Show grid", 
        value=st.session_state.show_grid
    )

def render_import_export():
    """
    Render import/export functionality.
    """
    st.header("Import/Export")
    
    export_tab, import_tab = st.tabs(["Export", "Import"])
    
    with export_tab:
        if st.button("Generate JSON"):
            json_data = export_curves_json()
            st.code(json_data, language="json")
            
            # Add download button
            st.download_button(
                label="Download JSON",
                data=json_data,
                file_name="bezier_curves.json",
                mime="application/json",
            )
    
    with import_tab:
        uploaded_file = st.file_uploader("Upload JSON file", type=["json"])
        
        if uploaded_file is not None:
            json_str = uploaded_file.getvalue().decode("utf-8")
            if st.button("Import JSON"):
                if import_curves_json(json_str):
                    st.success("JSON successfully imported")
                else:
                    st.error("Invalid JSON format")

def render_curve_visibility():
    """
    Render curve visibility toggles.
    """
    st.header("Visibility")
    
    # Create a horizontal layout for visibility checkboxes
    curve_names = list(st.session_state.curves.keys())
    cols_vis = st.columns(len(curve_names))
    
    for i, curve_name in enumerate(curve_names):
        with cols_vis[i]:
            st.session_state.curves[curve_name]["visible"] = st.checkbox(
                f"Show {curve_name}",
                value=st.session_state.curves[curve_name].get("visible", True),
                key=f"visible_{curve_name}"
            )

def render_sidebar():
    """
    Render the entire control sidebar.
    """
    st.header("Controls")
    
    # Get list of curve names
    curve_names = list(st.session_state.curves.keys())
    
    # Curve selection
    active_index = curve_names.index(st.session_state.active_curve) if st.session_state.active_curve in curve_names else 0
    
    active_curve = st.selectbox(
        "Edit Curve", 
        curve_names,
        index=active_index
    )
    st.session_state.active_curve = active_curve
    
    # Main tabs
    tabs = st.tabs(["Key Points", "CP1", "CP2", "CP3", "CP4", "Appearance"])
    
    # Key points tab
    with tabs[0]:
        render_key_points_tab(active_curve)
    
    # Control point 1 tab
    with tabs[1]:
        curve_config = st.session_state.curves[active_curve]
        render_control_point_editor(
            active_curve, 
            "cp1", 
            "Outgoing control point from start",
            "start_factor", 
            "start_height",
            f"This control point affects how the curve leaves the start point (x0={curve_config['x0']:.2f}, y=0)"
        )
    
    # Control point 2 tab
    with tabs[2]:
        curve_config = st.session_state.curves[active_curve]
        render_control_point_editor(
            active_curve, 
            "cp2", 
            "Incoming control point to peak",
            "peak_in_factor", 
            "peak_in_height",
            f"This control point affects how the curve approaches the peak point (x1={curve_config['x1']:.2f}, y={curve_config['max_y']:.2f})"
        )
    
    # Control point 3 tab
    with tabs[3]:
        curve_config = st.session_state.curves[active_curve]
        render_control_point_editor(
            active_curve, 
            "cp3", 
            "Outgoing control point from peak",
            "peak_out_factor", 
            "peak_out_height",
            f"This control point affects how the curve leaves the peak point (x1={curve_config['x1']:.2f}, y={curve_config['max_y']:.2f})"
        )
    
    # Control point 4 tab
    with tabs[4]:
        curve_config = st.session_state.curves[active_curve]
        render_control_point_editor(
            active_curve, 
            "cp4", 
            "Incoming control point to end",
            "end_factor", 
            "end_height",
            f"This control point affects how the curve approaches the end point (x2={curve_config['x2']:.2f}, y=0)"
        )
    
    # Appearance tab
    with tabs[5]:
        render_appearance_tab(active_curve)
    
    # Import/Export section
    render_import_export()
