Jenkins setup instructions

1. Install Python packages for the Jenkins build step

Add a build step (Execute Windows batch command) *before* running pytest:

```powershell
"C:\Users\reddy\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt
```

2. Run pytest with Allure and HTML reports

Use this command (note `--alluredir=allure-results`):

```powershell
"C:\Users\reddy\AppData\Local\Programs\Python\Python313\python.exe" -m pytest testcases -v --alluredir=allure-results --junitxml=result.xml --html=reports.html
```

3. Allure post-build

Ensure the Allure Jenkins post-build step points to `allure-results` (the directory from `--alluredir`). If your job currently passes a different directory, either update the pytest arg or change the Allure configuration accordingly.

4. Notes
- `--alluredir=allure-results` is the default directory name that Allure Jenkins expects. Using `report` requires updating the Allure step to read from `report`.
- Running `pip install -r requirements.txt` ensures `pytest-html` and `allure-pytest` are installed so pytest recognizes `--html` and `--alluredir` arguments.
