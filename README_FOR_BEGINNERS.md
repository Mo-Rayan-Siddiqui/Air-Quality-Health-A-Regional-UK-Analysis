# 🌟 A Beginner's Guide to the Air Quality & Health Project

Welcome! If you don't have a background in Computer Science or Data Science, don't worry. This guide is written specifically for you. It explains how you can explore this project, view the findings, and even run the interactive website on your own computer step-by-step.

---

## 1. The Easiest Way: View it Online! 🌐
You don't actually need to download anything to see the results. The interactive website is hosted online for free.

Simply click this link to see the interactive charts and read the findings:
**👉 [Live Interactive Website](https://nabeelvolt.github.io/Air-Quality-Health-A-Regional-UK-Analysis/)**

If you just want to read the written research report (without the code), click here:
**👉 [Full Research Report](./Full_Research_Report.md)**

---

## 2. Viewing the Project on Your Computer (Without Coding)
If you want to save the project to your computer and look at the charts offline, it's very easy:

### Step 1: Download the Project
1. Go to the top of this GitHub page.
2. Click the green **`<> Code`** button.
3. Click **Download ZIP**.
4. Once it downloads, find the ZIP file on your computer, right-click it, and select **Extract All...** to unzip it.

### Step 2: Open the Offline Report
1. Open the folder you just unzipped.
2. Double-click the file named **`blog.html`**. 
3. It will open in your web browser (like Chrome or Safari). This file contains the entire data science notebook, including all the maps and charts, fully rendered!

---

## 3. Running the Interactive Website on Your Computer
If you want to run the interactive website locally on your machine, you'll need to do a tiny bit of setup. Follow these exact steps:

### Step 1: Install Python
You need a program called Python to run the local server.
1. Go to [python.org/downloads](https://www.python.org/downloads/).
2. Click the big yellow **Download Python** button.
3. Run the installer. **IMPORTANT:** When the installer opens, make sure to check the box at the very bottom that says **"Add python.exe to PATH"** before you click Install.

### Step 2: Open the Command Prompt / Terminal
- **On Windows:** Press the `Windows` key, type `cmd`, and press Enter to open the Command Prompt.
- **On Mac:** Press `Command + Space`, type `Terminal`, and press Enter.

### Step 3: Go to the Project Folder
In the terminal, you need to navigate to the folder you unzipped earlier. 
Type `cd ` (with a space after it), then drag and drop the unzipped project folder directly into the terminal window, and press Enter.

### Step 4: Start the Website
Now, just type the following command and press Enter:
```text
python -m http.server 8080 --directory website
```
*Note: If you are on a Mac, you might need to type `python3` instead of `python`.*

### Step 5: View the Website!
Leave the black terminal window open. 
Open your web browser (Chrome, Edge, Safari) and type this exactly into the address bar at the top:
**`http://localhost:8080`**

You should now see the beautiful, interactive website running directly from your computer!

---

*Project authored by Rayan Siddiqui (May 2026).*
