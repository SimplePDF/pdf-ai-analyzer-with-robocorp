# PDF AI Analyzer with Robocorp

This automation is built using the following:
- [SimplePDF Robocorp integration](https://simplepdf.eu/help/how-to/using-the-robocorp-integration-to-analyse-your-documents-with-ai)
- [Robocorp's Python automation framework robo](https://github.com/robocorp/robo)
- [Robocorp's Vault](https://robocorp.com/docs/development-guide/variables-and-secrets/vault) to store the OpenAI API key
- [Robocorp's Asset Storage](https://robocorp.com/docs/control-room/asset-storage) to store the prompt

## How does it work?
_Interested in the step-by-step explanation? [Read the blog post](https://simplepdf.eu/help/how-to/use-the-robocorp-integration-to-leverage-ai-in-your-intelligent-document-processing-workflow)_

![Diagram](https://cdn.simplepdf.eu/simple-pdf/assets/help/robocorp-simplepdf-integration-openai-automation-diagram.png)


https://github.com/SimplePDF/pdf-ai-analyzer-with-robocorp/assets/10613140/9798f856-d840-4887-b1bd-bd73f2efcfc9



## How to use it?

1. [Get the robot on Robocorp Portal](https://robocorp.com/portal/robot/simplepdf/pdf-ai-analyzer-with-robocorp)
2. Configure the [SimplePDF Robocorp integration](https://simplepdf.eu/help/how-to/use-the-robocorp-integration-to-leverage-ai-in-your-intelligent-document-processing-workflow#configuring-the-integration)
3. Embed the document in your own app or website, or share the link to your customers: any submissions will automatically trigger the Robocorp process that will analyse the feedback


## Caveats

This automation works with [this document](https://cdn.simplepdf.eu/simple-pdf/assets/restaurant_feedback.pdf) only. Feel free to [adapt the logic](https://github.com/SimplePDF/pdf-ai-analyzer-with-robocorp/blob/main/tasks.py#L21) for your document
