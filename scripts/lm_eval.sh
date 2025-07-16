#!/bin/bash

MODEL_NAME=mamba2_hi
TRAIN_NAME=/Path/to/checkpoint
GPU=NUM_GPU
BATCH_SIZE=64

CUDA_VISIBLE_DEVICES=$GPU python -m eval.lm_harness_eval --model $MODEL_NAME \
                                --model_args pretrained=$TRAIN_NAME \
                                --tasks lambada_openai,piqa,hellaswag,winogrande,arc_easy,arc_challenge,wikitext \
                                --batch_size $BATCH_SIZE