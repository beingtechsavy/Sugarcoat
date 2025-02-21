# Sugarcoat - AI-powered Translator App

Welcome to **Sugarcoat**, an AI-powered translator app built using Azure Cognitive Services! Sugarcoat leverages the power of Azure's translation API to deliver fast, accurate, and polished translations in seconds. This app is designed for beginners who want to explore AI and cloud technologies in a simple and fun way.
Try it out here:- https://sugarcoat.azurewebsites.net/

---

## 🚀 Table of Contents
- [What is Sugarcoat?](#what-is-sugarcoat)
- [Why Sugarcoat?](#why-sugarcoat)
- [How to Get Started](#how-to-get-started)
- [Features](#features)
- [Deploying on Azure App Service](#deploying-on-azure-app-service)
- [Contributing](#contributing)
- [License](#license)

---

## What is Sugarcoat? 
**Sugarcoat** is a beginner-friendly app that uses **Azure Cognitive Services** to provide quick and accurate translations between various languages. Whether you're a student, developer, or AI enthusiast, Sugarcoat makes it easy to dive into the world of artificial intelligence and cloud technologies.

---

## Why Sugarcoat? 

- ✅ **Beginner-friendly**: Perfect for anyone new to AI or cloud development.
- ✅ **Built with Azure**: Leverage Microsoft’s powerful cloud tools for translation services.
- ✅ **Free for students**: If you have an **Azure Student Account**, you can build and deploy this app at no cost!
- ✅ **Quick to build**: The app can be built and deployed in under an hour!
- ✅ **Deployed on Azure App Service**: Hosted seamlessly on Azure, so you don’t need to worry about infrastructure.

---

## How to Get Started

1. **Clone the Repository:**

   Start by cloning the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/sugarcoat.git
   cd sugarcoat
   ```

2. **Install Dependencies:**

   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Azure Cognitive Services:**

   - Create a **Microsoft Azure** account if you don’t already have one.
   - Set up **Azure Cognitive Services** for translation.
   - Once you’ve created the service, you’ll receive an API key. 

4. **Configure the App:**

   Update the `config.py` or environment variables with your **Azure API key** and **endpoint URL**:
   ```python
   AZURE_API_KEY = 'your-api-key'
   AZURE_ENDPOINT = 'your-endpoint-url'
   ```

5. **Run the App Locally:**

   You can now run the app locally:
   ```bash
   python app.py
   ```

   Open your browser and visit `http://localhost:5000` to start using the translation app!

---

## Features

- **Translate text between languages**: Choose the source and target languages, and get your translation instantly.
- **Multiple language support**: Azure Cognitive Services supports a wide range of languages to choose from.
- **Simple, user-friendly interface**: A sleek and easy-to-navigate UI to get your translations quickly.

---

## Deploying on Azure App Service

Once you've set up and tested the app locally, it’s time to deploy it to Azure App Service. Follow these steps:

1. **Create an Azure App Service:**
   - Go to the [Azure Portal](https://portal.azure.com) and create a new **App Service**.
   - Choose the **Python** stack when prompted.
   
2. **Prepare your app for deployment:**

   - Ensure you have a `requirements.txt` file:
     ```bash
     pip freeze > requirements.txt
     ```

   - Create a **Procfile** to tell Azure how to run your app:
     ```
     web: gunicorn app:app
     ```

3. **Deploy to Azure App Service:**

   - If you haven’t installed the **Azure CLI** yet, you can do so from [here](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
   - Log in to your Azure account using:
     ```bash
     az login
     ```

   - Navigate to your app’s directory and deploy using Git:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     az webapp up --name your-app-name --resource-group your-resource-group --sku B1
     ```

4. **Access Your App:**

   Once the deployment is complete, you’ll receive a URL to access your app. Open the link in your browser and start translating text using Sugarcoat!

---

## Contributing

Sugarcoat is an open-source project, and contributions are always welcome! Here’s how you can get involved:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request

Let’s innovate together! 🚀

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

✨ **Your journey into AI starts here—let’s build something amazing with Azure!** ✨

--- 

(P.S. If you're a student, remember to use your **Azure Student Account** for free access to the Azure services used in this app!)
