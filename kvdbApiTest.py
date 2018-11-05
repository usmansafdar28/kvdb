import json
import unittest
import urllib.request as urllib2
import urllib

class KvdbApiTesting(unittest.TestCase):

    """
    All the Testcases written in form of Methods which executes in alphabetical order.
    if All the testcases Pass no error appears
    Ran XX tests in XXX seconds
    "OK" appears at the bottom
    """

    ## These Class Static variabales which can be accessed throughout this test suit for accessing Global Values
    
    bucket=''
    values = [1, 2, 3]
    data = {}
    url = 'https://kvdb.io'
    keyName = 'mykey'
    secretKey = 'mysecret'
    writeKey = 'myknock'
    default_ttl = 3600
    testCaseCounter=0;
    
    def setUp(self):
        
        KvdbApiTesting.testCaseCounter = KvdbApiTesting.testCaseCounter+1
        print("TestCase#:  ",KvdbApiTesting.testCaseCounter," Started")
        
       
    def test_aa_createSimpleBucket(self):
        '''
        This function creates a Bucket, if Bucket String length is equal to 22 characters this case considered as pass
        '''
        req = urllib2.Request(KvdbApiTesting.url, KvdbApiTesting.data,{'Content-Type': 'application/json'})
        f = urllib2.urlopen(req) ## Creating a New Bcket
        for x in f:
            KvdbApiTesting.bucket=x.decode('utf-8')
            print("Simple--- Bucket Created:", KvdbApiTesting.bucket)
        self.assertEqual(len(KvdbApiTesting.bucket),22)     ### Verifiy Bucket is created as per specs (String Lenght is 22 characters)

    def test_bb_updateBucketSecretKey(self):
        '''
        This function perform two jobs:
        1- update the Bucket with Secret key which then required to fetch the Bucket Keys.
        2- Send th JSON Data (after encoding in UTF-8) in the POST request.
        3- After POST request, if HTTP status Code is 200 then this Testcase is passed
        '''
        
        KvdbApiTesting.url = KvdbApiTesting.url + "/" + KvdbApiTesting.bucket + "/KEY?key=" + KvdbApiTesting.secretKey + "/" + KvdbApiTesting.keyName
        KvdbApiTesting.data = json.dumps(KvdbApiTesting.values).encode("utf-8")
        req = urllib2.Request(KvdbApiTesting.url, KvdbApiTesting.data,{'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        print("Status Code--- updateBucketSecretKey: ",f.getcode())
        self.assertEqual(f.getcode(),200)   ### Verify API response returns Success code 200

    def test_dd_retrieveWithoutSecretKey(self):
        '''
        This Function verifies that Key/Values cannot be retrieved without providing Secret key.
        If HTTP Status code is 404 then this Testcase is pass as URL cannot be found without secret key
        '''
        urlWithoutKey = 'https://kvdb.io/' +KvdbApiTesting.bucket+ "/" + KvdbApiTesting.keyName
        req = urllib2.Request(urlWithoutKey)   ## GET Request
        try:
            f = urllib2.urlopen(req)
            for x1 in f:
                fetchedResponse=x1.decode('utf-8')
        except urllib.error.HTTPError as errh:
            print("Status Code--- retrieveWithoutSecretKey: ",errh.code)
            self.assertEqual(errh.code,404)    
            
    def test_cc_getKeyValues(self):
        '''
        This Function verifies that Key/Values can be retrieved when Secret/Write Keys are provided.
        Assertion is applied on Response Received of the GET request and on the Data which we already POSTED for this Key
        '''
        fetchedResponse = ''
        req = urllib2.Request(KvdbApiTesting.url)   ## GET Request
        f = urllib2.urlopen(req)
        for x1 in f:
            fetchedResponse1=x1.decode('utf-8')
            fetchedResponse=x1
            print("Response--- getKeyValues", fetchedResponse1)
        self.assertEqual(fetchedResponse, KvdbApiTesting.data)    

    def test_ee_updateBucketSecretAndWriteKeys(self):
        '''
        This function perform three jobs:
        1- Updates the Bucket with Secret key which then required to fetch the Bucket Keys.
        2- Updates the Bucket with Write key which then required to fetch the Bucket Keys.
        3- Send th JSON Data (after encoding in UTF-8) in the POST request.
        4- "test_cc_getKeyValues" function is called to verify data is successfully posted and can be retrieved after updating the Keys.
        '''
        KvdbApiTesting.url = 'https://kvdb.io/' + KvdbApiTesting.bucket +"/KEY?key=" + KvdbApiTesting.secretKey + "/" + KvdbApiTesting.writeKey + "/" + KvdbApiTesting.keyName
        KvdbApiTesting.data = json.dumps(KvdbApiTesting.values).encode("utf-8")
        req = urllib2.Request(KvdbApiTesting.url, KvdbApiTesting.data,{'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        print("Status Code--- updateBucketSecretAndWriteKey: ",f.getcode())
        self.assertEqual(f.getcode(),200)   ### Verify API response returns Success code
        ###
        ### Now Calling "test_cc_retrieveWithKey" function to verify that data can be retrived with updated keys
        ###
        KvdbApiTesting.test_cc_getKeyValues(self)
        
    def test_ff_updateBucketDefaultTtl(self):
        '''
        1- This Function update the default_ttl value for the Bucket
        2- After POST request, if HTTP status Code is 200 then this Testcase is passed
        3- "test_cc_getKeyValues" function is called to verify data is successfully posted and can be retrieved after updating the Keys.
        '''
        
        KvdbApiTesting.url = 'https://kvdb.io/' + KvdbApiTesting.bucket +"/KEY?key=" + KvdbApiTesting.secretKey + "/" + KvdbApiTesting.writeKey + "/" + str(KvdbApiTesting.default_ttl) + "/" + KvdbApiTesting.keyName
        KvdbApiTesting.data = json.dumps(KvdbApiTesting.values).encode("utf-8")
        req = urllib2.Request(KvdbApiTesting.url, KvdbApiTesting.data,{'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        print("Status Code--- updateBucketDefaultTtl: ",f.getcode())
        self.assertEqual(f.getcode(),200)   ### Verify API response returns Success code
        ###
        ### Now Calling "test_cc_retrieveWithKey" function to verify that data can be retrived with updated keys
        ###
        KvdbApiTesting.test_cc_getKeyValues(self)
        
    def test_gg_getKeysList(self):
        '''
        This functions lists the key/values in the bucket (Secret key is required to access the data)
        Assertion: is applied on Response Received of the GET request and on the Data which we POSTED for this Key
        '''
        fetchedResponse = ''
        listKeysUrl = 'https://kvdb.io/' + KvdbApiTesting.bucket +"/KEY?key=" + KvdbApiTesting.secretKey +"/?values=true&format=json"
        req = urllib2.Request(listKeysUrl)   ## GET Request for Listing All Keys
        f = urllib2.urlopen(req)
        for x1 in f:
            fetchedResponse1=x1.decode('utf-8')
            fetchedResponse=x1
            print("Response--- getKeysList", fetchedResponse)
        self.assertEqual(fetchedResponse, KvdbApiTesting.data)
        
    def test_hh_deleteBucket(self):
        '''
        Bucket is Deleted in this function and Then GET request is made to verify it, if 404 Status code is found
        then testcase is pass.
        '''
        fetchedResponse = ''
        req = urllib2.Request(KvdbApiTesting.url)   ## GET Request for Listing All Keys
        req.get_method = lambda: 'DELETE'  ## Delete Method
        f = urllib2.urlopen(req)
        for x1 in f:
            fetchedResponse1=x1.decode('utf-8')
            fetchedResponse=x1
            print("Response--- deleteBucket", fetchedResponse)

        req = urllib2.Request(KvdbApiTesting.url)   ## GET Request After Deleting Bucket
        try:
            f = urllib2.urlopen(req)
            for x1 in f:
                fetchedResponse=x1.decode('utf-8')
        except urllib.error.HTTPError as errh:
            print("Status Code--- deleteBucket: ",errh.code)
            self.assertEqual(errh.code,404) ### Verify API response returns Status code 404 (Not Found)
            
    def tearDown(self):
        print("TestCase#: ", KvdbApiTesting.testCaseCounter,"  Executed")

if __name__ == "__main__":
    unittest.main()
