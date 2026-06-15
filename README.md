# Signal Processing Utilities

A small collection of educational Python scripts for basic signal processing tasks: convolution and Fourier series visualization.

**Overview**
- **Purpose:**: Provide simple, easy-to-follow implementations of convolution and Fourier series concepts for learning and quick experimentation.
- **Language:**: Python 3

**Files**
- **README:**: Overview and usage instructions ([README.md](README.md#L1))
- **Convolution implementation:**: [convolution.py](convolution.py)
- **Fourier series demo:**: [fourier-series.py](fourier-series.py)
- **Dependencies:**: [requirements.txt](requirements.txt)

**Requirements**
- Python 3.8+ recommended.
- Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Usage**

- Run the convolution example:

```bash
python convolution.py
```

- Run the Fourier series demo:

```bash
python fourier-series.py
```

Each script includes inline usage notes and example functions — open the files to see available entry points and parameters.

**What each script does**
- **convolution.py**: Demonstrates discrete convolution between signals, includes helper functions to create example signals and visualize results.
- **fourier-series.py**: Builds and visualizes Fourier series approximations for common periodic signals (e.g., square, sawtooth), showing partial-sum convergence.

**Examples**
- To convolve two example signals from within a Python REPL:

```python
from convolution import example_convolution
result = example_convolution()
```

- To compute a Fourier series approximation programmatically:

```python
from fourier_series import approximate_square
approx = approximate_square(terms=25)
```

**Next steps / ideas**
- Add Jupyter notebooks with interactive plots.
- Add unit tests for numerical correctness.
- Expand README with sample images and timing benchmarks.

**License**
- MIT — feel free to reuse and adapt for learning purposes.

---
