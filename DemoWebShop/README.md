To run test on desired browser
 pytest -s -v testCases/ --browser firefox
 pytest -s -v testCases/ --browser chrome


To generate HTML Report
pytest -s -v --html=Reports/report.html testCases/ --browser chrome



# Summary:
- test should consist only from part which is really under test. All preparation should be done in preconditions
- test should have some steps and asserts of expected results to check if something was really done. 
    The same approach as we do in manual testing: do something -> check result, do another thing -> check another result
- missing full verification
- test data and expected data should be in test, not in page logic 
- missing requirements