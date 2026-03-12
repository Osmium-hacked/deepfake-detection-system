const express = require("express");
const axios = require("axios");
const cors = require("cors");
const multer = require("multer");
const fs = require("fs");
const FormData = require("form-data");

const app = express();
app.use(cors());

const upload = multer({ dest: "uploads/" });
const AI_SERVICE_URL = "http://localhost:8000";

app.get("/health", (req, res) => {
  res.json({ status: "Backend running" });
});

app.post("/analyze", upload.single("file"), async (req, res) => {
  if (!req.file) {
  return res.status(400).json({ error: "No file uploaded" });
}
console.error("AI Error:", error.message);

  try {
    const formData = new FormData();
    formData.append(
      "file",
      fs.createReadStream(req.file.path)
    );

    const response = await axios.post(
      `${AI_SERVICE_URL}/predict`,
      formData,
      {
        headers: formData.getHeaders()
      }
    );
    const confidenceText =
      response.data.confidence > 0.75
    ? "High confidence"
    : response.data.confidence > 0.55
    ? "Medium confidence"
    : "Low confidence";


    fs.unlinkSync(req.file.path); // cleanup
    res.json({
  ...response.data,
  confidenceLevel: confidenceText,
});
  } catch (error) {
    res.status(500).json({
      error: "AI service failed",
      details: error.message
    });
  }
});

app.listen(4000, () => {
  console.log("Backend running on port 4000");
});
