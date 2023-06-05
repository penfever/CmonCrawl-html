#!/bin/bash
for file in /scratch/bf996/datasets/commoncrawl/*/*.html
do
    cmon extract --n_proc=8 "/scratch/bf996/CmonCrawl/html_extractor/config.json" "/scratch/bf996/datasets/commoncrawl/extracted_output" "$file" html
done