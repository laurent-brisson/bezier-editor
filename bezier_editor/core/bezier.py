#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bezier curve mathematical functions.

This module provides the core functionality for calculating and creating
bezier curves with different control points configurations.
"""

import numpy as np

def cubic_bezier(t, p0, p1, p2, p3):
    """
    Calculate points on a cubic Bezier curve.
    
    Args:
        t (np.array): Parameter values between 0 and 1
        p0, p1, p2, p3: Control points for the cubic Bezier curve
        
    Returns:
        np.array: Points on the curve at parameter values t
    """
    return (1-t)**3 * p0 + 3*(1-t)**2 * t * p1 + 3*(1-t) * t**2 * p2 + t**3 * p3

def generate_controlled_curve(key_points, control_points, num_points=1000):
    """
    Generate a curve passing through key points with explicit control points.
    
    Args:
        key_points (list): List of (x,y) tuples defining key points
        control_points (list): List of (x,y) tuples defining control points
        num_points (int): Total number of points to generate along the curve
        
    Returns:
        tuple: (x_points, y_points) as numpy arrays
    """
    if len(key_points) < 2:
        raise ValueError("At least two key points are needed")
    
    expected_control_points = 2 * (len(key_points) - 1)
    if len(control_points) != expected_control_points:
        raise ValueError(f"Incorrect number of control points: {len(control_points)} "
                         f"provided, {expected_control_points} expected")
    
    x_curve = []
    y_curve = []
    
    points_per_segment = num_points // (len(key_points) - 1)
    
    for i in range(len(key_points) - 1):
        p0 = np.array(key_points[i])
        p3 = np.array(key_points[i+1])
        
        p1 = np.array(control_points[2*i])      # Control point out from p0
        p2 = np.array(control_points[2*i+1])    # Control point in to p3
        
        t = np.linspace(0, 1, points_per_segment)
        x_segment = cubic_bezier(t, p0[0], p1[0], p2[0], p3[0])
        y_segment = cubic_bezier(t, p0[1], p1[1], p2[1], p3[1])
        
        x_curve.extend(x_segment)
        y_curve.extend(y_segment)
    
    return np.array(x_curve), np.array(y_curve)

def create_simple_bezier_curve(x0, x1, x2, max_y, control_config):
    """
    Create a simple Bezier curve passing through three points with configurable control points.
    
    Args:
        x0, x1, x2: X coordinates of the start, peak, and end points
        max_y: Y coordinate of the peak point
        control_config (dict): Configuration parameters for control points
        
    Returns:
        tuple: (key_points, control_points) where each is a list of (x,y) coordinates
    """
    key_points = [(x0, 0), (x1, max_y), (x2, 0)]
    
    d1 = x1 - x0  # Distance from start to peak
    d2 = x2 - x1  # Distance from peak to end
    
    control_points = [
        # Outgoing control point from first point
        (x0 + d1 * control_config['start_factor'], 
         max_y * control_config['start_height']),
        
        # Incoming control point to peak
        (x1 - d1 * control_config['peak_in_factor'], 
         max_y * control_config['peak_in_height']),
        
        # Outgoing control point from peak
        (x1 + d2 * control_config['peak_out_factor'], 
         max_y * control_config['peak_out_height']),
        
        # Incoming control point to end point
        (x2 - d2 * control_config['end_factor'], 
         max_y * control_config['end_height'])
    ]
    
    return key_points, control_points
