# joy-ride-content-app

This repository is responsible for implementing generic Joyride component for app startpages. The repo contains .json files for the apps or modules we need to add the joy ride funcationality inside.

The the name of the json file should fellow the following naming schema: joy-ride-{App_Name}.json.

Inside the file, we are initialising the following properties for every joy ride step:

id: accepts the number of the step.
title: the English title of the step.
title_de: the German title of the step.
content: the English content of the step.
content_de: the German content of the step.
target: the target HTML element that the step should display on the page,
placement: the position of the joy ride step on the page.


The sample layout of the Json file should be like the following : 

[
    {
    "id": 1,
    "title": "Step 1",
    "title_de": "Shritt 1",
    "content": "This is step 1",
    "content_de": "Das ist schritt 1",
    "target": ".container-fluid",
    "placement": "center"
    },
    {
    "id": 2,
    "title": "Step 2",
    "title_de": "Shritt 2",
    "content": "This is step 2",
    "content_de": "Das ist schritt 2",
    "target": ".container-fluid",
    "placement": "center"
    },
]
