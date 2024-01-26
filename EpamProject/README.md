To run test on desired browser
 pytest -s -v testCases/ --browser firefox
 pytest -s -v testCases/ --browser chrome


To generate HTML Report
pytest -s -v --html=Reports/report.html testCases/ --browser chrome
