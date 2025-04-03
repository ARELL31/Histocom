# Histocom - Commit History Manager 📜🔍

[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Open Source](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://opensource.org)

A Python-powered commit history visualization and management tool with intuitive reporting capabilities.

## 🌟 Features

- **Comprehensive Commit Analysis**: Track SHA hashes, authors, timestamps, and associated issues
- **Intuitive GUI**: User-friendly Tkinter interface for seamless interaction
- **Smart Reporting**: Automatically generate Excel reports with:
  - Commit metadata analysis
  - Issue tracking correlations
  - Modified files inventory
- **Time Zone Awareness**: Native support for local time zone conversions
- **Open Standards**: Compatible with Git workflows and Excel formats

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git installed on system PATH

### Installation

1. Clone the repository:
```bash
git clone https://mmedia1.fi-b.unam.mx/git/LuisF/histocom.git
cd histocom
```
2. Create and activate virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
## 🖥️ Usage
1. Launch the application:
```bash
python histocom/main.py
```
3. Select your Git repository directory through the GUI
  - Generate and export reports:
  - Choose output format (Excel by default)
  - Customize time zone settings
  - Filter commits by date range or author
## 🤝 Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/amazing-feature
```
3. Commit your changes:
4. Push to the branch:
5. Open a Pull Request
  - **Please read our Contribution Guidelines for details.**
## 📜 License
**This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.**
## 📚 Documentation
Full documentation available at docs/README.md
