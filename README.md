# PDF AI Analyzer with Robocorp

This automation is built using the following:
- [SimplePDF Robocorp integration](https://simplepdf.eu/help/how-to/using-the-robocorp-integration-to-analyse-your-documents-with-ai)
- [Robocorp's Python automation framework robo](https://github.com/robocorp/robo)
- [Robocorp's Vault](https://robocorp.com/docs/development-guide/variables-and-secrets/vault) to store the OpenAI API key
- [Robocorp's Asset Storage](https://robocorp.com/docs/control-room/asset-storage) to store the prompt

## How does it work?
_Interested in the step-by-step explanation? [Read the blog post](https://simplepdf.eu/help/how-to/use-the-robocorp-integration-to-analyse-your-pdf-document-submissions-with-ai)_

![Diagram](https://cdn.simplepdf.eu/simple-pdf/assets/help/robocorp-simplepdf-integration-openai-automation-diagram.png)

## Caveats

This automation works with [this document](https://cdn.simplepdf.eu/simple-pdf/assets/restaurant_feedback.pdf) only. Feel free to adapt the logic for your document