Feature: Fizzbuzz Test
    Scenario: Returns Fizz
        Given Fizzbuzz app is run
        When I input "6"
        Then I get result "Fizz"
        
    Scenario: Returns Buzz
        Given Fizzbuzz app is run
        When I input "10"
        Then I get result "Buzz"

    Scenario: Returns FizzBuzz
        Given Fizzbuzz app is run
        When I input "15"
        Then I get result "FizzBuzz"

    Scenario: Returns Fizz
        Given Fizzbuzz app is run
        When I input "2"
        Then I get result "None"

    Scenario: Returns Fizz
        Given Fizzbuzz app is run
        When I input "fizz"
        Then I get "ValueError"