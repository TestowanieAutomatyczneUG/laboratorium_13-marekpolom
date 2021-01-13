Feature: Friendships Test

    @data
    Scenario: Adds friendships
        Given Friendships app is run
            """
            Kowalski,Nowak
            """
        When I input "Kowalski" and "Nowak"
        Then I get result "Kowalski" is friend of "Nowak"
        Then And "Nowak" is friend of "Kowalski"

    @data
    Scenario: Adds 2 friendships
        Given Friendships app is run
            """
            Kowalski,Andrzejewicz,Kwiatkowski
            """
        When I input "Kowalski" and "Andrzejewicz"
        When I input "Kowalski" and "Kwiatkowski"
        Then I get result "Kowalski" is friend of "Andrzejewicz"
        Then And "Andrzejewicz" is friend of "Kowalski"
        Then I get result "Kowalski" is friend of "Kwiatkowski"
        Then And "Kwiatkowski" is friend of "Kowalski"

    @data
    Scenario: Adds 2 same friendships
        Given Friendships app is run
            """
            Jakub,Marek
            """
        When I input "Jakub" and "Marek"
        When I again input "Jakub" and "Marek"
        Then I get result "Already friends!"

    @data
    Scenario: Get friends list
        Given Friendships app is run
            """
            Jakub,Ola,Marek
            """
        When I input "Jakub" and "Ola"
        When And I input "Jakub" and "Marek"
        When I get friends list of "Jakub"
        Then I get result "Marek, Ola"

    @data
    Scenario: Check if they are friends
        Given Friendships app is run
            """
            Ola,Marek
            """
        When I input "Ola" and "Marek"
        When I check if "Ola" and "Marek" are friends
        Then I get result "True"

    @data
    Scenario: Check if they are friends
        Given Friendships app is run
            """
            Ola,Marek,Jakub
            """
        When I input "Ola" and "Jakub"
        When I check if "Marek" and "Jakub" are friends
        Then I get result "False"

    @data
    Scenario: Get friends list
        Given Friendships app is run
            """
            Adam,Jan,Tomek
            """
        When I input "Adam" and "Jan"
        When I input "Tomek" and "Adam"
        When I check friends list of "Adam"
        Then I get result "Jan, Tomek"

    @data
    Scenario: Get friends list
        Given Friendships app is run
            """
            Adam,Jan,Tomek,Kasia
            """
        When I input "Jan" and "Tomek"
        When I input "Jan" and "Adam"
        When I check friends list of "Kasia"
        Then I get result ""