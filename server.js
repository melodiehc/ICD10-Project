require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const OpenAI = require('openai');

const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'ICD_10.html'));
});


const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.post('/predict', async (req, res) => {
  const note = req.body.note;

  try {
    const chatCompletion = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "user",
          content: `Suggest the most relevant ICD-10 codes for the following clinical note:\n"${note}"`
        }
      ]
    });

    const responseText = chatCompletion.choices[0].message.content;
    const codes = responseText.match(/[A-Z]\d{2}(\.\d+)?/g); // Simple ICD-10 regex

    res.json({ codes: codes || [] });
  } catch (error) {
    console.error("Error:", error);
    res.status(500).json({ error: "Something went wrong on the server." });
  }
});

app.listen(port, () => {
  console.log(` Server is running on http://localhost:${port}`);
});
