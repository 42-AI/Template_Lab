<div align="center">

# 42AI - Lab Template

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/ashleve/lightning-hydra-template"><img alt="Template" src="https://img.shields.io/badge/-Lightning--Hydra--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>
[![Paper](http://img.shields.io/badge/paper-arxiv.1001.2234-B31B1B.svg)](https://www.nature.com/articles/nature14539)
[![Conference](http://img.shields.io/badge/AnyConference-year-4b44ce.svg)](https://papers.nips.cc/paper/2020)

</div>

## Description

This is 42AI Lab Template.

Created from [ashleve/lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)

This template is Research Ready.
It will allow for fast and high quality experiment, development, and results analysis.


There is still some work to do such that we can make it production ready.

For high quality inference these next steps seems wise:
 - Adding ONNX support
 - Docker compliant
 - Fast API server

## How to run

Install dependencies

```bash
# clone project
git clone https://github.com/42-AI/Template_Lab
cd Template_Lab

# Setup the repository
.42AI/init.sh
```

Train model with default configuration

```bash
# train on CPU
python train.py trainer.gpus=0

# train on GPU
python train.py trainer.gpus=1
```

Train model with chosen experiment configuration from [configs/experiment/](configs/experiment/)

```bash
python train.py experiment=experiment_name.yaml
```

You can override any parameter from command line like this

```bash
python train.py trainer.max_epochs=20 datamodule.batch_size=64
```

Multi run experiment
```bash
python train.py -m experiment=fashion_conv "++model.net.dropout=range(0,.5,.1)" "++model.lr=1e-2,1e-3"
```
