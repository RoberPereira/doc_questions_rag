
# ASK QUESTION TO YOUR_DOC 

Ask question to your documents

## Best Results 
### document: xLSTM paper
### notebook: exp_chunk800 
#### chunk_size 800 - overlap 400
### Question:
**What are the major improvements over the previous LSTM architecture?**

> SIMILARITY
>- Exponential gating and novel memory structures
>- Introduction of sLSTM with scalar memory, scalar update, and memory mixing
>- Introduction of mLSTM with matrix memory and covariance update rule
>- Fully parallelizable architecture
>- Linear computation and constant memory complexity with respect to sequence length
>- Compressive memory well suited for industrial applications and edge implementations
 
> MMR
>- Introduction of exponential gating with appropriate normalization and stabilization techniques
>- Modification of LSTM memory structure to include sLSTM with scalar memory, scalar update, and new memory mixing, and mLSTM with matrix memory and covariance update rule
>- Integration of these LSTM extensions into residual block backbones to create xLSTM blocks and
architectures

> COMPRESSION  
>- The major improvements over the previous LSTM architecture are the introduction of exponential gating and novel memory structures, including the sLSTM with scalar memory and update, and the mLSTM with matrix memory and covariance update rule.


## Others results obtained
### document: xLSTM paper 
### notebook: exp_chunk500_nobulletpoint
#### chunk_size 500 - overlap 200 - promt with and without asking for bullet points summary

### Question: **What are the major improvements over the previous or vanilla LSTM architecture?**
#### 1) Without asking for bullet point summary and chunk_size 500

- SIMILARITY
> The major improvements over the previous or vanilla LSTM architecture include the introduction of exponential gating with appropriate normalization and stabilization techniques, modification of the LSTM memory structure to obtain sLSTM and mLSTM variants, and integration of these LSTM extensions into the xLSTM architecture. These improvements have been shown to significantly boost performance in language modeling tasks.

- COMPRESSION
> The major improvements over the previous or vanilla LSTM architecture include replacing every second LSTM layer with a non-gated feed-forward network with GeLU activation function, adding Exponential Gating to this architecture, and integrating these LSTM extensions such as sLSTM and mLSTM. These improvements also involve modifying the LSTM memory structure, using pre-LayerNorm residual backbones, and incorporating a post up-projection block and a matrix memory.

### Question: **What are the major improvments over the previous LSTM arquitecture summarize in bullet points?**
#### 2) Asking for bullet point summary and chunk_size 500

- Using similarity vector retriever 
>- Exponential gating with normalization and stabilization techniques
>- Modification of LSTM memory structure, resulting in sLSTM and mLSTM variants
>- Fully parallelizable mLSTM with matrix memory and covariance update rule

- Using compression vector retriever 
>- Introduction of exponential gating with normalization and stabilization techniques
>- Modification of LSTM memory structure to include sLSTM with scalar memory and update, and mLSTM with matrix memory and covariance update rule
>- These extensions allow for better handling of long context problems and improved efficiency in language modeling.


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

Add your OpenAi Token to .env file:  
```bash
echo OPENAI_API_KEY=\'{your_token}\' > .env
```


## Usage
- Add your document in data\raw\ directory
- modify config.py with your:
  - file_name:
  - model: gpt-3.5-turbo (default)
  - chunk_size : 800 (default)
  - chunk_overlap : 400 (default)
- modify template (at your convenience)
- use the notebook:
```bash
run.ipynb
```
