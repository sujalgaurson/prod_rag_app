'use client'

import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  files?: File[]
  timestamp: Date
}

interface ChatMessageProps {
  message: Message
}

export function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === 'user'

  return (
    <div
      className={`flex w-full mb-4 animate-fadeIn ${
        isUser ? 'justify-end' : 'justify-start'
      }`}
    >
      <div className={`flex flex-col max-w-[85%] md:max-w-[70%] ${isUser ? 'items-end' : 'items-start'}`}>
        {/* File attachments */}
        {message.files && message.files.length > 0 && (
          <div className="mb-2 flex flex-wrap gap-2">
            {Array.from(message.files).map((file, index) => (
              <div
                key={index}
                className="px-3 py-1.5 bg-gray-100 dark:bg-gray-800 rounded-lg text-sm text-gray-700 dark:text-gray-300 flex items-center gap-2"
              >
                <svg
                  className="w-4 h-4"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  />
                </svg>
                <span className="truncate max-w-[200px]">{file.name}</span>
              </div>
            ))}
          </div>
        )}

        {/* Message bubble */}
        <div
          className={`rounded-xl px-4 py-3 shadow-sm ${
            isUser
              ? 'bg-blue-500 text-white'
              : 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100'
          }`}
        >
          {isUser ? (
            <p className="text-sm whitespace-pre-wrap break-words">{message.content}</p>
          ) : (
            <div className="prose prose-sm dark:prose-invert max-w-none">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                className="text-sm"
                components={{
                  p: ({ children, ...props }) => <p className="mb-2 last:mb-0" {...props}>{children}</p>,
                  ul: ({ children, ...props }) => <ul className="list-disc pl-5 mb-2" {...props}>{children}</ul>,
                  ol: ({ children, ...props }) => <ol className="list-decimal pl-5 mb-2" {...props}>{children}</ol>,
                  li: ({ children, ...props }) => <li className="mb-1" {...props}>{children}</li>,
                  code: ({ children, className, ...props }) => {
                    const isInline = !className || typeof className !== 'string' || !className.includes('language')
                    return isInline ? (
                      <code className="bg-gray-200 dark:bg-gray-700 px-1 py-0.5 rounded text-xs" {...props}>
                        {children}
                      </code>
                    ) : (
                      <code className="block bg-gray-200 dark:bg-gray-700 p-2 rounded text-xs overflow-x-auto" {...props}>
                        {children}
                      </code>
                    )
                  },
                  pre: ({ children, ...props }) => (
                    <pre className="bg-gray-200 dark:bg-gray-700 p-2 rounded text-xs overflow-x-auto mb-2" {...props}>
                      {children}
                    </pre>
                  ),
                }}
              >
                {message.content}
              </ReactMarkdown>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
