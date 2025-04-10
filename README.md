# Distributed Fourier Series Computation System

##  Overview

This project implements a **Distributed System** that computes the **Fourier Series** of a given function over a specified interval. The computation of Fourier coefficients is distributed among multiple worker nodes to improve performance and demonstrate concepts in distributed computing.

Ideal for projects combining **mathematics**, **parallel processing**, and **distributed systems** concepts.

## System Architecture

- **Client:** Takes user input (function, interval, number of terms).
- **Main Server (Coordinator):** 
  - Splits the computation into subtasks.
  - Distributes tasks to multiple **Worker Servers**.
  - Aggregates results and returns the final Fourier Series.

- **Worker Servers:**
  - Compute specific Fourier coefficients (an, bn) based on assigned ranges.
  - Return results to the Main Server.

## Features

- Supports periodic functions (e.g., sin(x), cos(x), square waves).
- Parallel coefficient computation.
- Scalable architecture with pluggable worker nodes.
- Optional visualization of the original function and its Fourier approximation.

## Fourier Series Formula

For a periodic function \( f(x) \) defined on \([-L, L]\), the Fourier series is:

\[
f(x) \approx \frac{a_0}{2} + \sum_{n=1}^{N} \left(a_n \cos\left(\frac{n\pi x}{L}\right) + b_n \sin\left(\frac{n\pi x}{L}\right)\right)
\]

where:

\[
a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos\left(\frac{n\pi x}{L}\right) dx,\quad
b_n = \frac{1}{L} \int_{-L}^{L} f(x) \sin\left(\frac{n\pi x}{L}\right) dx
\]
