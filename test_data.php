#!/usr/bin/python

testData = '''

#marina ul.test {
    list-style-type: none;
    color: white;
    background: black;
}

#marina ul.test .list-item a {
    text-decoration: none;
<<<<<<< HEAD:test_data.py
    color: #737373;
}

#my_element ul.test .list-item:last-child {
    font-weight: bold;
}'''
=======
}
";
>>>>>>> master:test_data.php

expectedOutput = '''

#my_element {


    h1 {
        font-weight: bold;
    }

    ul.test {
        list-style-type: none
        color: white;
        background: black;

        .list-item {
            text-decoration: none;
            color: #737373;
        }

        .list-item:last-child {
            font-weight: bold;
        }
    }
<<<<<<< HEAD:test_data.py
}'''
=======
}";
>>>>>>> master:test_data.php
