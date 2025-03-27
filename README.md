# Bezier Curve Editor

An interactive application for creating, manipulating, and comparing multiple Bezier curves.

![Bezier Curve Editor Screenshot](https://github.com/laurent-brisson/bezier-editor/blob/main/bezier_editor_screenshot.png?raw=true)

## Features

- Display multiple predefined curves simultaneously
- Fine adjustment of curve parameters with small steps
- Color selection for each curve
- JSON import/export functionality
- CSV data export for all visible curves
- Organized UI with intuitive tab structure

## Installation

### From PyPI (recommended)

```bash
pip install bezier-editor
```

### From Source

1. Clone the repository
```bash
git clone https://github.com/yourusername/bezier-editor.git
cd bezier-editor
```

2. Install the package
```bash
pip install -e .
```

## Usage

### Launch the application

```bash
bezier-editor
```

Or if installed from source:

```bash
streamlit run bezier_editor/app.py
```

### Basic UI Overview

The application is divided into two main sections:

1. **Control Panel (Left):** Adjust parameters for each curve
   - Key Points: Set the start, peak, and end positions
   - Control Points: Fine-tune the curve shape
   - Appearance: Change colors and visualization options

2. **Visualization (Right):** Interactive graph showing all curves
   - Display multiple curves simultaneously
   - Show/hide control points and handles
   - Export data as CSV

### Working with Curves

- **Select a curve to edit** from the dropdown menu
- Use **slider controls** for quick adjustments or **number inputs** for precise values
- Toggle visibility of individual curves using the checkboxes
- Export your creations to JSON for future use or sharing

### Using as a Library

The `bezier-editor` package can also be used as a library in your own Python scripts. Here's how to import and use its main functionalities:

```python
# Import core mathematical functions
from bezier_editor.core.bezier import cubic_bezier, generate_controlled_curve, create_simple_bezier_curve

# Get predefined configurations
from bezier_editor.core.presets import get_presets, ensure_float

# Use input/output functions
from bezier_editor.io.file_operations import prepare_curves_for_csv_export

# Example: create and calculate a curve
presets = get_presets()
curve_config = presets['Curve 1']

# Create a simple Bezier curve
key_points, control_points = create_simple_bezier_curve(
    curve_config['x0'], 
    curve_config['x1'], 
    curve_config['x2'], 
    curve_config['max_y'], 
    curve_config['control_config']
)

# Generate points on the curve
x_points, y_points = generate_controlled_curve(key_points, control_points, num_points=500)

# Use the points for visualization, analysis, or export
import matplotlib.pyplot as plt
plt.plot(x_points, y_points)
plt.show()
```

## Development

### Project Structure

```
bezier-editor/
├── bezier_editor/
│   ├── core/         # Mathematical functions
│   ├── io/           # File operations
│   ├── ui/           # User interface components
│   └── app.py        # Main application
├── tests/            # Unit tests
└── examples/         # Example configurations
```

### Running Tests

```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
