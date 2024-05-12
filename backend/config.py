azure_endpoint1 = "YOUR AZURE ENDPOINT"
api_version1 = "2024-02-15-preview"

parse_instructions = '''
For the next prompt, take in consideration the following rules and process the data accordingly:    
&nbsp;    
All user stories specify conditions that must be met before the main action of the story can take place. For example, in User Story A, the pre-condition is that the user has accessed an FO form​​.    
Actor(s):    
&nbsp;    
Each story identifies the "User" as the primary actor who interacts with the system to achieve a goal. This consistent actor across the stories emphasizes user-centric design​​.    
Post-conditions:    
&nbsp;    
The outcomes that should be achieved after the actions described in the user story are completed. For example, in User Story C, the post-condition is that the system saves the personal reference on the current form​​.    
Requirements:    
&nbsp;    
Detailed descriptions of what needs to be done to fulfill the user story. These can include specific functionalities or features that the system must have. For instance, User Story B outlines requirements for specifying and changing application languages​​.    
Information Model:    
&nbsp;    
This includes the data elements that are involved in the user story, often detailing field labels, descriptions, types, and visibility. It helps define the structure of data and interaction within the system for the given user story​​​​​​.    
Messages:    
&nbsp;    
Defined messages that may be shown to the user during the interaction with the system. These messages can be informative, warnings, or errors, helping guide the user's actions or inform them of the system's state. For example, User Story C includes tooltip and disclaimer messages related to the personal reference field​​.    
&nbsp;    
Now acknowledge these rules and do the provided text based on the rules.
'''

output_instructions = '''
As an output follow this structure: 
{
    “title”: “example”,
    “testCases”: [
        {
            “testCaseId”: “example”,
            “title”: “example”,
            “description”: “example“,
            “preConditions”: [
                “example“,
                “example”
            ],
            “requirement”: [“example”],
            “actions”: [
                {
                    “step”: “example“,
                    “expectedResults”: [
                        “example“,
                        “example”
                    ]
                },
                {
                    “step”: “example”,
                    “expectedResults”: [
                        “example“,
                        “example”
					
                    ]
                }
            ]
        }
    ]
}

testCaseId - all test cases should have the same acronym related to the user story followed by an hifen and a unique number.
title - brief description of the case events.
description - should describe what happens in the test case.
preConditions - conditions related to the specific test case.
requirement - the requirement present on the user stories, id only.
actions - interactions the user has with the app.
step - description of a specific interaction.
expectedResults - all possible application behaviours regarding the users actions.


Create twice as many test cases and interactions that the user can have with the application compared to what youd initially create, if possible, alwaysn write more than 2 actions.
In the same ammount, create test cases following a happy path and an unhappy path.

Create the test cases based on how a professional tester would document every single action it performs while testing the application.
'''
