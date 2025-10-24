#!/bin/bash
source "$(dirname "$0")/env/bin/activate"
python "$(dirname "$0")/API_Ingestion.py"