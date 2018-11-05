# kvdb
KVDB's REST API testing using PYTHON

# Python Modules Used:
    1- json (Sending Json data in POST requests)
    2- unittest (Testing Framework which gives the capability for compiling, asserting and executing the Test Suits)
    3- urllib (This Module is being used for sending HTTP's POST, GET, UPDATE and DELETE REST reuests and receive responses)
# Python Version used for Development:
    3.7.1
# How to RUN the Tests
    Open the "kvdbApiTest" file in python IDE and Press "F5"
# Main Class:
    "KvdbApiTesting" is main class which extends the "unittest.TestCase" class
    - All the Testcases are written in the form of Methods which executes in alphabetical order.
    - If All the testcases Pass no error appears, result Appear as:
    - Ran XX tests in XXX seconds
    - "OK" appears at the bottom
# Methods in the Class:
    Here are eight methods created to cover the API testing scope which executes in Alphabetical order. 
    Each method starts with "test" keywword which is unittest module naming convention requirement for methods to be considered for auto     execution:
  # 1- test_aa_createSimpleBucket(self):
            This function creates a Bucket, Asserion is applied on Bucket String length, if its is equal to 22 characters this case                   considered as pass
  # 2- test_bb_updateBucketSecretKey(self):
             This function perform three jobs:
              1- update the Bucket with Secret key which then required to fetch the Bucket Keys.
              2- Send the JSON Data (after encoding in UTF-8) in the POST request.
              3- Assertion: After POST request, if HTTP status Code is 200 then this Testcase is pass
  # 3- test_dd_retrieveWithoutSecretKey(self):
              This Function verifies that Key/Values cannot be retrieved without providing Secret key.
              Assertion: If HTTP Status code is 404 then this Testcase is pass as URL cannot be found without providing secret key
  # 4- test_cc_getKeyValues(self):
              This Function verifies that Key/Values can be retrieved when Secret Key is provided.
              Assertion: is applied on Response Received of the GET request and on the Data which we POSTED for this Key

  # 5- test_ee_updateBucketSecretAndWriteKeys(self):
              This function perform following multiple jobs:
              1- Updates the Bucket with Secret key which then required to fetch the Bucket Keys.
              2- Updates the Bucket with Write key which then required to write in the Bucket.
              3- Send the JSON Data (after encoding in UTF-8) in the POST request.
              4- Assertion 1: After POST request, if HTTP status Code is 200 then this Testcase is pass
              5- Assertion 2: "test_cc_getKeyValues" function is called to verify data is successfully posted and can be retrieved after                  updating the Keys.
  # 6- test_ff_updateBucketDefaultTtl(self):
              1- This Function update the default_ttl value for the Bucket
              2- Assertion 1: After POST request, if HTTP status Code is 200 then this Testcase is passed
              3- Assertion 2: "test_cc_getKeyValues" function is called to verify data is successfully posted and can be retrieved after                  updating the default_ttl.
  # 7- test_gg_getKeysList(self):
              This functions lists the key/values in the bucket (Secret key is required to access the data)
              Assertion: is applied on Response Received of the GET request and on the Data which we POSTED for this Key
  # 8- test_hh_deleteBucket(self):
              Bucket is Deleted in this function 
              Assertion: GET request is made to verify Bucket does not exists and 404 Status code is returned.
              then testcase is pass.


