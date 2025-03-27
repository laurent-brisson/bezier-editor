#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the core bezier curve functions.
"""

import unittest
import numpy as np
from bezier_editor.core.bezier import cubic_bezier, generate_controlled_curve, create_simple_bezier_curve

class TestBezierFunctions(unittest.TestCase):
    """Test cases for bezier curve functions."""
    
    def test_cubic_bezier(self):
        """Test cubic bezier function."""
        # Test at t=0, should be equal to p0
        t_0 = np.array([0])
        p0, p1, p2, p3 = 1, 2, 3, 4
        result = cubic_bezier(t_0, p0, p1, p2, p3)
        self.assertEqual(result[0], p0)
        
        # Test at t=1, should be equal to p3
        t_1 = np.array([1])
        result = cubic_bezier(t_1, p0, p1, p2, p3)
        self.assertEqual(result[0], p3)
        
        # Test for multiple t values
        t_values = np.array([0, 0.5, 1])
        result = cubic_bezier(t_values, p0, p1, p2, p3)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], p0)
        self.assertEqual(result[2], p3)
    
    def test_generate_controlled_curve(self):
        """Test generate_controlled_curve function."""
        # Simple test with two key points
        key_points = [(0, 0), (1, 1)]
        control_points = [(0.25, 0.25), (0.75, 0.75)]
        
        x_curve, y_curve = generate_controlled_curve(key_points, control_points, num_points=100)
        
        # Check result shapes and lengths
        self.assertEqual(len(x_curve), 100)
        self.assertEqual(len(y_curve), 100)
        
        # Check start and end points
        self.assertAlmostEqual(x_curve[0], key_points[0][0])
        self.assertAlmostEqual(y_curve[0], key_points[0][1])
        self.assertAlmostEqual(x_curve[-1], key_points[1][0])
        self.assertAlmostEqual(y_curve[-1], key_points[1][1])
        
        # Test with invalid inputs
        with self.assertRaises(ValueError):
            # Not enough key points
            generate_controlled_curve([(0, 0)], [])
        
        with self.assertRaises(ValueError):
            # Incorrect number of control points
            generate_controlled_curve([(0, 0), (1, 1)], [(0.5, 0.5)])
    
    def test_create_simple_bezier_curve(self):
        """Test create_simple_bezier_curve function."""
        # Define parameters
        x0, x1, x2 = 0, 5, 10
        max_y = 6
        control_config = {
            "start_factor": 0.4, "start_height": 0.2,
            "peak_in_factor": 0.3, "peak_in_height": 0.9,
            "peak_out_factor": 0.3, "peak_out_height": 0.9,
            "end_factor": 0.4, "end_height": 0.2
        }
        
        # Create curve
        key_points, control_points = create_simple_bezier_curve(x0, x1, x2, max_y, control_config)
        
        # Check key points
        self.assertEqual(len(key_points), 3)
        self.assertEqual(key_points[0], (x0, 0))
        self.assertEqual(key_points[1], (x1, max_y))
        self.assertEqual(key_points[2], (x2, 0))
        
        # Check control points
        self.assertEqual(len(control_points), 4)
        
        # First control point
        d1 = x1 - x0
        self.assertEqual(control_points[0], (x0 + d1 * control_config['start_factor'], 
                                           max_y * control_config['start_height']))

if __name__ == '__main__':
    unittest.main()
