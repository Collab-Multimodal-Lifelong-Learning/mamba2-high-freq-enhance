# Mitigating Over-Smoothing in Mamba2 via Spectral Domain Analysis

📝 [Paper](https://openreview.net/forum?id=r08kqzrito)

We introduce simple High-Frequency Enhancement method to mitigate over-smoothing in Mamba2.


# Setup
## Create Environment
To set up our environment, please run:
```
conda env create -f environment.yaml
conda activate mamba_hi
```

Install Mamba:
```
pip install mamba-ssm==2.2.2
pip install causal-conv1d
```

## Additional Requirements - lm_harness_eval
```
pip install lm_eval==0.4.2
```

# Evaluation
To evaluate our model, you should first download the checkpoint from this URL.

TBD

To run language modeling and commonsense reasoning benchmarks:
```
sh scripts/lm_eval.sh 
```
You can modify arguments in config file. The primary values are the best hyperparameter values.

