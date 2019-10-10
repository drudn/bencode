1) save the file bencode.py to the same directly as your script, then import it into your own script by calling import bencode.py


2) the library has the following methods:
   convert() accepts a bencode string representing one of four native types in python; integer, byte string, list or    dictionary and returns the corresponding value in python   
   toInteger() accepts a string value representing an integer in bencode, and returns its corresponding python    integer value 
   toByteString() accepts a string value representing a string in bencode, and returns its corresponding python    string value


*input arguments are assumed to be written in proper bencode
 dictionaries/lists should have the same number of keys as values which can only be composed of bencode integers and  strings 
    
  