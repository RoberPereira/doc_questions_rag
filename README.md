
# APP NAME 

A

## Installation

Python version==3.11.5

Start virtual enviroment. [venv](https://docs.python.org/3/library/venv.html#venv-def)
```bash
python -m venv .venv
source .venv/bin/activate
```

Use pip-tools package manager to install project dependencies. [pip-tools](https://pip-tools.readthedocs.io/en/stable/)
```bash
python -m pip install pip-tools
```

To install dependencies from requirements.in run: 
```bash
pip-compile requirements.in
pip install -r requirements.txt

```

## Usage

```bash
python run.ipynb
```

## Some results obtained

### Question:
**What are the major improvments over the previous or vanilla LSTM arquitecture?**

- Using similarity vector retriever 
> The major improvements over the previous or vanilla LSTM architecture include the introduction of exponential gating with appropriate normalization and stabilization techniques, modification of the LSTM memory structure to obtain sLSTM and mLSTM variants, and integration of these LSTM extensions into the xLSTM architecture. These improvements have been shown to significantly boost performance in language modeling tasks.

- Using compression vector retriever 
> The major improvements over the previous or vanilla LSTM architecture include replacing every second LSTM layer with a non-gated feed-forward network with GeLU activation function, adding Exponential Gating to this architecture, and integrating these LSTM extensions such as sLSTM and mLSTM. These improvements also involve modifying the LSTM memory structure, using pre-LayerNorm residual backbones, and incorporating a post up-projection block and a matrix memory.

### Question:
**What are the major improvments over the previous LSTM arquitecture summarize in bullet points?**

- Using similarity vector retriever 
>- Exponential gating with normalization and stabilization techniques
>- Modification of LSTM memory structure, resulting in sLSTM and mLSTM variants
>- Fully parallelizable mLSTM with matrix memory and covariance update rule

- Using compression vector retriever 
>- Introduction of exponential gating with normalization and stabilization techniques
>- Modification of LSTM memory structure to include sLSTM with scalar memory and update, and mLSTM with matrix memory and covariance update rule
>- These extensions allow for better handling of long context problems and improved efficiency in language modeling.