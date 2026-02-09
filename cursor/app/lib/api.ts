// const API_BASE = "http://localhost:8000"
// Instead of http://localhost:8000

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://13.60.186.81:8000";

export async function uploadFile(file: File) {
  const formData = new FormData()
  formData.append("file", file)

  const res = await fetch(`${API_BASE}/upload`, {
    method: "POST",
    body: formData,
  })

  if (!res.ok) {
    throw new Error("File upload failed")
  }

  return res.json()
}

export async function queryRag(question: string) {
  const res = await fetch(
    `${API_BASE}/query?question=${encodeURIComponent(question)}`,
    {
      method: "POST",
    }
  )

  if (!res.ok) {
    throw new Error("Query failed")
  }

  return res.json()
}
