#a1
#Mingjin Liu
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""


currency_from=input("the currency on hand")
currency_to=input("the currency to convert to")
amount_from=float(input("amount of currency to convert"))  


def has_error(json):
    """Returns: True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the opposite of 
    the value following the keyword "success". For example, if the JSON is

    '{"from":"","to":"","success":false,"error":"Source currency code is 
    invalid."}'
    then the query is not valid, so this function returns True (It does NOT 
    return the message 'Source currency code is invalid').
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    jud=json.split('"')
    jud1=jud[10]
    jud2=jud1[1:6]
    if jud2=="false":
        judgement="true"
    else:
        judgement="false"
    return judgement
        

def the_result(json):
    """Returns: the money you change
    json:the string you get from URL"""
    resu=json.split('"')
    resu1=resu[7]
    resu2=resu1.split()
    fin=resu2[0]
    return fin


def make_url(currency_from, currency_to, amount_from):
    """Returns:A string you get from URL
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url1='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from)

    from urllib.request import urlopen

    doc = urlopen(url1)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    json=make_url(currency_from, currency_to, amount_from)
    jum=has_error(json)
    if jum=="false":
        final_money=the_result(json)
    else:
        final_money="What you input is wrong."
    return final_money

print(exchange(currency_from, currency_to, amount_from))


if __name__=="__exchange__":    
    exchange()   

def testA():
    """test has_error"""
    a=has_error('{ "from" : "25 United States Dollars", "to" : "14420.919025 Costa Rican Col\u00f3nes", "success" : true, "error" : "" }')
    if a=="false":
        b="true"
    else:
        b="false"
    return b


def testB():
    """test the_result"""
    c=the_result('{ "from" : "25 United States Dollars", "to" : "14420.919025 Costa Rican Col\u00f3nes", "success" : true, "error" : "" }')
    if c=="14420.919025":
        d="true"
    else:
        d="false"
    return d
    

def testC():
    """test make_url"""
    e=make_url('USD','CRC',25)
    if e=='{ "from" : "25 United States Dollars", "to" : "14420.919025 Costa Rican Col\u00f3nes", "success" : true, "error" : "" }':
        f="true"
    else:
        f="false"
    return f


def testD():
    """test exchange"""
    g=exchange('USD','CRC',25)
    if g=="14420.919025":
        h="true"
    else:
        h="false"
    return h


def testAll():
    """test all cases"""
    testA()
    testB()
    testC()
    testD()
    print("All tests passed")
        