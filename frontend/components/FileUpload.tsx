
import { useState } from "react";

export default function FileUpload() {
  const [status, setStatus] = useState("");

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    setStatus("Uploading...");

    const res = await fetch("http://localhost:8000/api/upload", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setStatus(data.message || "Upload complete");
  };

  return (
    <div>
      <input type="file" onChange={handleUpload} />
      <p>{status}</p>
    </div>
  );
}
