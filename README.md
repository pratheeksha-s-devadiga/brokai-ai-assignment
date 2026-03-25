# AI Lead Intelligence System

## Overview
This project is a multi-agent AI system that automates lead processing from raw Excel data.

It takes a list of companies and:
- Researches company information
- Extracts contact details
- Generates personalized outreach messages

The goal is to convert raw lead data into actionable insights for business outreach.

---

## System Architecture

The system is designed using three independent agents:

### 1. Research Agent
- Searches the web using DuckDuckGo
- Extracts company summary and website
- Applies filtering to remove irrelevant sources
- Uses fallback logic when no data is found

### 2. Contact Finder Agent
- Extracts email and phone from Excel and web
- Cleans and formats contact information
- Handles missing or invalid data gracefully

### 3. Outreach Writer Agent
- Generates personalized outreach messages
- Uses company name and summary
- Falls back to generic messaging when needed

---

## Features

- Multi-agent architecture (modular and scalable)
- Graceful failure handling (no crashes)
- Automatic data cleaning and formatting
- Excel to structured output pipeline
- Streamlit UI for easy interaction
- CSV export with proper formatting

---

## Tech Stack

- Python
- Streamlit
- Pandas
- DuckDuckGo Search
