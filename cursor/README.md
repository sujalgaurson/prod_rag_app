# RAG Assistant - ChatGPT-like Frontend

A modern, responsive ChatGPT-like frontend for RAG (Retrieval Augmented Generation) applications built with Next.js, React, and Tailwind CSS.

## Features

- 💬 **Chat Interface**: Human ↔ AI conversation layout similar to ChatGPT
- 📁 **File Upload**: Support for PDF, DOCX, and TXT files
- 🌓 **Theme Toggle**: Light and dark mode with localStorage persistence
- ✨ **Smooth Animations**: Fade-in and slide-in animations for messages
- 📱 **Responsive Design**: Works seamlessly on mobile and desktop
- 📝 **Markdown Support**: AI responses support markdown formatting
- ⌨️ **Keyboard Shortcuts**: Press Enter to send, Shift+Enter for new line
- 🔄 **Typing Indicator**: Visual feedback while waiting for AI response

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm

### Installation

1. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

2. Run the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
├── app/
│   ├── components/
│   │   ├── ChatArea.tsx       # Scrollable chat message list
│   │   ├── ChatMessage.tsx    # Individual message component
│   │   ├── Header.tsx         # App header with theme toggle
│   │   ├── InputBar.tsx       # Input area with file upload
│   │   ├── ThemeProvider.tsx  # Theme context provider
│   │   ├── ThemeToggle.tsx    # Theme toggle button
│   │   └── TypingIndicator.tsx # Loading animation
│   ├── globals.css            # Global styles
│   ├── layout.tsx             # Root layout
│   └── page.tsx               # Main page component
├── package.json
├── tailwind.config.ts
└── tsconfig.json
```

## Customization

### Connecting to Your Backend

Replace the mock API call in `app/page.tsx` with your actual backend endpoint:

```typescript
const handleSend = async (content: string, files: File[]) => {
  // ... create user message ...

  // Upload files and send query to your API
  const formData = new FormData()
  files.forEach(file => formData.append('files', file))
  formData.append('query', content)

  const response = await fetch('/api/rag', {
    method: 'POST',
    body: formData,
  })

  const data = await response.json()
  
  // Create AI message with response
  const aiMessage: Message = {
    id: Date.now().toString(),
    role: 'assistant',
    content: data.response,
    timestamp: new Date(),
  }

  setMessages((prev) => [...prev, aiMessage])
  setIsTyping(false)
}
```

### Styling

The app uses Tailwind CSS with custom dark mode support. Modify colors and styles in:
- `tailwind.config.ts` - Theme configuration
- `app/globals.css` - Global CSS variables
- Component files - Component-specific Tailwind classes

## Technologies Used

- **Next.js 14** - React framework with App Router
- **React 18** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS framework
- **react-markdown** - Markdown rendering for AI responses
- **remark-gfm** - GitHub Flavored Markdown support

## License

MIT
