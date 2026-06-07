# InsightSeg Project Setup Guide

## Prerequisites

* Python 3.12
* Git
* GitHub Account

## Clone Repository

```bash
git clone https://github.com/MayukhDas2004/InsightSeg.git
cd InsightSeg
```

## Create Virtual Environment

```bash
py -3.12 -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Verify TensorFlow

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

## Git Workflow

* Never work directly on main
* Use dev branch
* Create feature branches from dev
* Commit frequently
* Push changes regularly

## Team Structure

* Member 1 → AI Model Development
* Member 2 → Infrastructure & Deployment
* Member 3 → Visualization & Evaluation
* Member 4 → Documentation & Literature Review
