'use client'

import { useState, useEffect, useRef } from 'react'
import { ThemeProvider } from './components/ThemeProvider'
import { Header } from './components/Header'
import { ChatArea } from './components/ChatArea'
import { InputBar } from './components/InputBar'
import { Message } from './components/ChatMessage'
import { uploadFile, queryRag } from "./lib/api"

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([])
  const [isTyping, setIsTyping] = useState(false)
  const timeoutRef = useRef<NodeJS.Timeout | null>(null)

  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current)
      }
    }
  }, [])

  const handleSend = async (content: string, files: File[]) => {
    if (!content.trim() && files.length === 0) return
  
    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content: content || "Uploaded file(s)",
      timestamp: new Date(),
    }
  
    setMessages((prev) => [...prev, userMessage])
    setIsTyping(true)
  
    try {
      // 1️⃣ Upload files (if any)
      for (const file of files) {
        await uploadFile(file)
      }
  
      // 2️⃣ Query RAG
      const res = await queryRag(content)
  
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: res.answer,
        timestamp: new Date(),
      }
  
      setMessages((prev) => [...prev, aiMessage])
    } catch (err: any) {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now().toString(),
          role: "assistant",
          content: `❌ Error: ${err.message}`,
          timestamp: new Date(),
        },
      ])
    } finally {
      setIsTyping(false)
    }
  }

  return (
    <ThemeProvider>
      <div className="flex flex-col h-screen bg-white dark:bg-gray-900">
        <Header />
        <ChatArea messages={messages} isTyping={isTyping} />
        <InputBar onSend={handleSend} disabled={isTyping} />
      </div>
    </ThemeProvider>
  )
}
