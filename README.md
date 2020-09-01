# joy-ride-content-app

This repository is used for applying a generic approach of Joyride component for app start pages. The repo contains JSON files for the apps or modules we need to add the joy ride functionality inside. If you make any commits please check I your editor(for example Visual Studio Code) shows any warning regarding the JSON files.

## Prerequisites

* [Git](https://git-scm.com/download/win)
* [Visual Studio Code](https://code.visualstudio.com/download)
  * With the following extensions:
    * [Insert GUID](https://marketplace.visualstudio.com/items?itemName=heaths.vscode-guid)

## Helpful Links for Visual Studio Code

* [Getting the Repository on your PC](https://code.visualstudio.com/docs/editor/github)
* [Using Git](https://code.visualstudio.com/docs/editor/versioncontrol)
* [Using Insert GUID](https://devblogs.microsoft.com/setup/insert-guids-directly-into-visual-studio-code/)

## Directory-Structure

```text
.
+-- routes.json
+-- product1
|   +-- joy-ride-training.json
|   +-- joy-ride-documentManagment.json
+-- product2
|   +-- joy-ride-tasks.json
```

## product

Products are represented as folders and should contain one or more tours.

### joy-ride-{appname}.json

**IMPORTANT** Each tour requires a unique ID. Use the Insert GUID Extension for this. Versions should only be incremented when the tour content is updated and **not** when spelling mistakes are corrected, because after each version increment the tour will be shown the user again. Keep $schema unchanged!

Those files represent the tour itself. Please start qmbase/template.json as template for any tour and then just add your steps. To add a new step just look how the other steps are defined and add the step behind the last one by adding a comma and copy the new step after the comment.


### Step Format
- id: accepts the number of the step.
- title: the title of the step in HTML
-- de: German version
-- en: English version
- content: the content of the step in HTML
-- de: German version
-- en: English version
- target: A CSS selector allows selecting an HTML element where the step will be displayed
- placement: Where at the target the step will be shown. An editor with JSON schema support will list all currently available options for this step.

### routes.json

Is an index for all tours which should be activated. **Please ensure the names and ids match the one specified in the tours.**


## Basic HTML Formatting

- Start: <>
- End: </>
- <>Content</>
- Tag References: https://www.w3schools.com/html/default.asp
- `<b>and this is bold text</b>` <- This will be bold
- `<b>` Bold
- `<p>` Paragraph
- `<a href=‘https://google.de’>` Link
- `<i>` italic
- `<img src=‘https://www.qmbase.com/wp-content/uploads/2016/07/Left_logo_qmBase_w298px.png’/>` Image
- `<span role='img' aria-label='Konfetti‘>❤</span>`  <- any emoticons

## N.B: If the new language is not specified for title or content attributes, the default English values will be displayed

## Joyride Options

https://github.com/gilbarbara/react-joyride
