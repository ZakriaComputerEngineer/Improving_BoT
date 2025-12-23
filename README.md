# Enhanced Buffer of Thoughts (BoT) Proof-of-Concept

## Overview
This project implements enhancements to the Buffer of Thoughts (BoT) framework. The original BoT proposal uses a single-template retrieval mechanism based on semantic similarity. This implementation introduces two core modifications to improve reasoning accuracy and architectural stability.

## Identified Limitation
The primary limitation in the original BoT framework is Structural-Semantic Mismatch. Semantic embedding models often fail to distinguish between the topic of a text and the logic required to solve it. Furthermore, the discrete retrieval of a single template prevents the model from addressing hybrid problems that require multiple reasoning structures simultaneously.

## Proposed Solutions

### 1. Dynamic Template Composition (DTC)
Instead of selecting the single best match, the system retrieves the top-k templates and synthesizes them into a task-specific synthetic template. This allows the integration of diverse reasoning steps (e.g., combining mathematical solving with logical constraint verification).

### 2. Active Buffer Governance (ABG)
To prevent buffer degradation and redundancy, this system introduces:
- **Fitness Scoring:** Templates are weighted based on their historical success in solving queries.
- **Automated Pruning:** A maintenance process removes suboptimal or failing templates from the meta-buffer.

## Components
- **Problem Distiller:** Extracts variables, constraints, and logic types from raw queries.
- **Governance Buffer Manager:** Manages template storage, weighted retrieval, and fitness updates.
- **Template Composer:** Merges multiple retrieved templates into a unified reasoning structure.
- **BoT Engine:** Orchestrates the workflow from distillation to feedback.

## Setup and Usage
The Proof-of-Concept is written in Python and does not require external dependencies for basic execution.

### Execution
```bash
python main.py
```
