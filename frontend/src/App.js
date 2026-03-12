import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const handleSubmit = async () => {
    if (!file) return alert("Please select an image");
    if (!res.ok) {throw new Error("Server error");
    }


    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setResult(null);

   setError(null);

  try {
  const res = await fetch("http://localhost:4000/analyze", {
    method: "POST",
    body: formData,
  });

  if (!res.ok) throw new Error("Analysis failed");

  const data = await res.json();
  setResult(data);
} catch (err) {
  setError("Failed to analyze image. Please try again.");
} finally {
  setLoading(false);
}

  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Deepfake Detection</h1>

      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Image"}
      </button>

      <br /><br />

      {result && (
        <div>
          <h3>Result:</h3>
          <p><strong>Prediction:</strong> {result.prediction}</p>
          <p><strong>Confidence:</strong> {result.confidence}</p>
        </div>
      )}
    </div>
  );
}

export default App;
