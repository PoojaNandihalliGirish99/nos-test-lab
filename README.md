# Network OS Testing Lab 🚀

## Tech Stack

- Containerlab (network topology simulation)
- FRRouting (FRR) for BGP routing
- pyATS for test automation
- Docker for containerized network nodes
- Python for automation scripts

## Features

- Multi-router BGP topology
- Automated validation using pyATS
- Custom parser for FRR CLI output
- Genie integration attempt with fallback logic

## Architecture

Containerlab → FRR Routers → BGP → pyATS Tests → Validation