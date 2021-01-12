Feature: Roman Test
    Scenario: Returns I
        Given Roman app is run
        When I input "1"
        Then I get result "I"
        
    Scenario: Returns IV
        Given Roman app is run
        When I input "4"
        Then I get result "IV"

    Scenario: Returns V
        Given Roman app is run
        When I input "5"
        Then I get result "V"

    Scenario: Returns XXVII
        Given Roman app is run
        When I input "27"
        Then I get result "XXVII"

    Scenario: Returns XCIII
        Given Roman app is run
        When I input "93"
        Then I get "XCIII"

    Scenario: Returns CLXIII
        Given Roman app is run
        When I input "163"
        Then I get "CLXIII"

    Scenario: Returns DLXXV
        Given Roman app is run
        When I input "575"
        Then I get "DLXXV"

    Scenario: Returns MXXIV
        Given Roman app is run
        When I input "1024"
        Then I get "MXXIV"

    Scenario: Returns XCIII
        Given Roman app is run
        When I input "3000"
        Then I get "MMM"