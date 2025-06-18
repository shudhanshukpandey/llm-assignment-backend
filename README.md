# llm-assignment-backend


# 🚀 FastAPI Backend Setup Guide

This guide helps you set up and run a FastAPI backend using either `venv` or `conda` for environment management. It also includes steps to run the server with `uvicorn`.

---

## 📦 Requirements

- Python 3.8 or higher
- `pip` or `conda`
- `git` (optional, if cloning the repo)

---

## 📁 Project Structure (Example)

```
|-llm_services
|-src
|   |-app_core
|   |-models
|   |-routers
|   |-schemas
|   |-services
|   |-app.py
|-main.py
|-requirements.py
```

---

## 🐍 Option 1: Using `venv` (Python Virtual Environment)

### 🔹 Create Virtual Environment

```bash
python -m venv venv
```

### 🔹 Activate Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐍 Option 2: Using `conda`

### 🔹 Create Conda Environment

```bash
conda env create -f environment.yml
```

### 🔹 Activate Environment

```bash
conda activate fastapi-env
```

> Make sure `environment.yml` exists with required dependencies (sample provided below).

---

## ▶️ Running the FastAPI App with Uvicorn

### 🔹 Basic Run

```bash
uvicorn main:app --reload
```

- `--reload` enables auto-reload on code changes (useful in development)
- Make sure `main.py` contains something like:


### 🔹 Run with Host and Port

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📦 `requirements.txt` (for venv)

```
fastapi
uvicorn[standard]
```

Add other dependencies as needed.

---

## 📦 `environment.yml` (for conda)

```yaml
name: fastapi-env
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.9
  - pip
  - pip:
      - fastapi
      - uvicorn[standard]
```

---

## ✅ Testing

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  
Interactive Swagger docs available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧹 Deactivate Environment

- `venv`: `deactivate`
- `conda`: `conda deactivate`

---

## 🗑 Optional Cleanup

To remove the virtual environment:

- `venv`: Delete the `venv/` folder.
- `conda`: Run `conda env remove -n fastapi-env`

---

## 📌 Notes

- Use `.env` or config management for secrets (e.g. database URLs, API keys).
- Consider using `gunicorn` and `nginx` in production setups.

---

