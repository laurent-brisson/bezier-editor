#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the IO functions (file operations).
"""

import unittest
import json
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
from bezier_editor.io.file_operations import prepare_curves_for_csv_export

class TestIOFunctions(unittest.TestCase):
    """Test cases for IO functions."""
    
    def test_prepare_curves_for_csv_export(self):
        """Test prepare_curves_for_csv_export function."""
        # Test with empty data
        empty_data = {}
        result = prepare_curves_for_csv_export(empty_data)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)
        
        # Test with actual curve data
        curve_data = {
            'Curve 1': {
                'x': np.array([0.0, 0.5, 1.0]),
                'y': np.array([0.0, 0.7, 0.0])
            },
            'Curve 2': {
                'x': np.array([0.0, 0.25, 0.5, 0.75, 1.0]),
                'y': np.array([0.0, 0.2, 0.5, 0.2, 0.0])
            }
        }
        
        result = prepare_curves_for_csv_export(curve_data)
        
        # Check result structure
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 5)  # Should match the longest curve
        self.assertEqual(len(result.columns), 4)  # 2 curves × 2 dimensions
        
        # Check column names
        expected_columns = ['Curve 1_x', 'Curve 1_y', 'Curve 2_x', 'Curve 2_y']
        for col in expected_columns:
            self.assertIn(col, result.columns)
        
        # Check padding for shorter curve
        self.assertTrue(np.isnan(result['Curve 1_x'].iloc[3]))
        self.assertTrue(np.isnan(result['Curve 1_y'].iloc[4]))
        
        # Check actual values
        self.assertEqual(result['Curve 1_x'].iloc[0], 0.0)
        self.assertEqual(result['Curve 1_y'].iloc[1], 0.7)
        self.assertEqual(result['Curve 2_x'].iloc[2], 0.5)
        self.assertEqual(result['Curve 2_y'].iloc[4], 0.0)

# We can't easily test export_curves_json and import_curves_json
# without mocking Streamlit session state, but those would be good
# candidates for additional tests with proper mocking.

if __name__ == '__main__':
    unittest.main()
